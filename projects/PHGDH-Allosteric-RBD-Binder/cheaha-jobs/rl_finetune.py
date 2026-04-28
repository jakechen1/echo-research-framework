#!/usr/bin/env python
"""Round 5: REINFORCE / PPO fine-tune of pretrained transformer with composite reward.

Reward signal (computed at sample time on each generated SMILES):
  reward = w_aff * affinity_score(smiles)         # DrugCLIP-PHGDH or Vina proxy
        + w_dl  * (qed - 0.5)                     # drug-likeness
        + w_nov * novelty(smiles)                 # 1 - max Tanimoto vs known actives
        - w_inv * (0 if rdkit_valid else 1)       # invalid penalty (mostly redundant w/ SELFIES)
        - w_sa  * (sa_score - 4) / 4              # synthetic accessibility soft penalty

Policy gradient with KL-penalty to pretrained prior (prevents distribution collapse):
  loss = -E[reward * log_prob] + beta * KL(policy || prior)

Entropy regularization (prevents mode collapse):
  loss += -lambda_ent * H(policy_distribution)

Usage:
  rl_finetune.py \
    --pretrain runs/round4_pretrain_<jobid>/best.pt \
    --vocab runs/round4_pretrain_<jobid>/vocab.json \
    --known-actives /data/user/$USER/aim4_clm/bucket_pv5.smi \
    --reward-fn drugclip_phgdh   # or 'vina_quick' (tox21-like quick-score) or 'qed_only' (debug)
    --out runs/round5_rl_<jobid> \
    --batch 64 --steps 2000 --lr 1e-5 \
    --beta-kl 0.1 --lambda-ent 0.01 \
    --w-aff 1.0 --w-dl 0.3 --w-nov 0.3 --w-inv 1.0 --w-sa 0.1

Notes:
- Loads the pretrained transformer weights (frozen as `prior` for KL ref + trainable `policy` copy).
- DrugCLIP-PHGDH reward is a placeholder; once trained (Track B), wire it in via --reward-fn.
- For Round 5 development without DrugCLIP: use --reward-fn qed_only to verify the RL loop.
"""
from __future__ import annotations
import argparse, copy, csv, json, math, random, sys, time
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical

# Reuse model from Round 4
sys.path.insert(0, str(Path(__file__).parent))
from pretrain_transformer import SmallTransformer, PAD, START, END

try:
    import selfies as sf
except ImportError:
    sf = None

try:
    from rdkit import Chem
    from rdkit.Chem import AllChem, QED, DataStructs
    from rdkit.Chem import Descriptors, Crippen, Lipinski
    from rdkit.Contrib.SA_Score import sascorer
    from rdkit import RDLogger
    RDLogger.DisableLog("rdApp.*")
except ImportError:
    Chem = None
    sascorer = None


# ----------------------- Reward functions -----------------------

class RewardFn:
    """Composite reward over a batch of (selfies, smiles) tuples."""

    def __init__(self, args, known_fps=None, chemberta=None):
        self.args = args
        self.known_fps = known_fps or []
        self.chemberta = chemberta

    def __call__(self, smiles_batch):
        rewards = []
        # Batch ChemBERTa once if active (much faster than per-molecule)
        cb_scores = None
        if self.chemberta is not None and self.args.reward_fn == "chemberta":
            try:
                cb_scores = self.chemberta.score([s if s else "C" for s in smiles_batch]).cpu().tolist()
            except Exception as e:
                print(f"[chemberta] batch-score failed: {e}", flush=True)
                cb_scores = None
        for smi in smiles_batch:
            r = 0.0
            mol = Chem.MolFromSmiles(smi) if Chem and smi else None
            if mol is None:
                rewards.append(-self.args.w_inv)
                continue
            # Drug-likeness
            qed = QED.qed(mol)
            r += self.args.w_dl * (qed - 0.5)
            # Novelty
            if self.known_fps:
                fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, 2048)
                sims = DataStructs.BulkTanimotoSimilarity(fp, self.known_fps)
                novelty = 1.0 - (max(sims) if sims else 0.0)
                r += self.args.w_nov * novelty
            # SA penalty
            if sascorer:
                try:
                    sa = sascorer.calculateScore(mol)
                    r -= self.args.w_sa * max(0, sa - 4.0) / 4.0
                except Exception:
                    pass
            # Affinity (placeholder)
            if self.args.reward_fn == "qed_only":
                r += self.args.w_aff * (qed - 0.5)  # equivalent to extra QED weight
            elif self.args.reward_fn == "drugclip_phgdh":
                # TODO: wire DrugCLIP-PHGDH score here once trained (Track B)
                # For now: stub returning 0; safe to leave until DrugCLIP ready
                r += 0.0
            elif self.args.reward_fn == "vina_quick":
                # TODO: cheap Vina-proxy via cached lookup
                r += 0.0
            elif self.args.reward_fn == "chemberta":
                if cb_scores is not None:
                    # Center on 0.5 (rough threshold separating actives from decoys per smoke test)
                    # Range typically 0.3 (decoy) to 0.9 (active); subtract 0.5 then weight
                    r += self.args.w_aff * (cb_scores[len(rewards)] - 0.5)
            rewards.append(r)
        return torch.tensor(rewards, dtype=torch.float32)


# ----------------------- Sampling -----------------------

@torch.no_grad()
def sample_with_log_probs(model, max_len, vocab_size, bos_id, eos_id, pad_id, batch_size, device, temperature=1.0):
    """Sample sequences and return (token_ids [B,T], log_probs [B,T], lens [B])."""
    seq = torch.full((batch_size, 1), bos_id, dtype=torch.long, device=device)
    log_probs_list = []
    finished = torch.zeros(batch_size, dtype=torch.bool, device=device)
    for t in range(max_len - 1):
        logits = model(seq) / max(temperature, 1e-6)
        next_logits = logits[:, -1, :]
        dist = Categorical(logits=next_logits)
        next_tok = dist.sample()
        log_probs_list.append(dist.log_prob(next_tok))
        # If finished, force PAD
        next_tok = torch.where(finished, torch.full_like(next_tok, pad_id), next_tok)
        seq = torch.cat([seq, next_tok.unsqueeze(1)], dim=1)
        finished = finished | (next_tok == eos_id) | (next_tok == pad_id)
        if finished.all():
            break
    log_probs = torch.stack(log_probs_list, dim=1)  # [B, T-1]
    return seq, log_probs


def decode_to_smiles(token_ids: torch.Tensor, i2tok: dict, eos_id: int, pad_id: int) -> list[str]:
    """Convert token tensor to SMILES strings via SELFIES decode."""
    out = []
    for row in token_ids:
        toks = []
        for tid in row.tolist():
            if tid in (eos_id, pad_id):
                break
            if tid < 3:  # PAD / BOS / EOS / etc.
                continue
            toks.append(i2tok.get(tid, ""))
        sel_str = "".join(t for t in toks if t)
        try:
            smi = sf.decoder(sel_str) if sf else ""
        except Exception:
            smi = ""
        out.append(smi)
    return out


# ----------------------- KL to prior -----------------------

def kl_to_prior(policy_logits, prior_logits):
    """KL(policy || prior) per token, averaged."""
    p = F.log_softmax(policy_logits, dim=-1)
    q = F.log_softmax(prior_logits, dim=-1)
    pp = p.exp()
    return (pp * (p - q)).sum(-1).mean()


# ----------------------- Main -----------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pretrain", required=True, type=Path)
    ap.add_argument("--vocab", required=True, type=Path)
    ap.add_argument("--known-actives", type=Path, default=None)
    ap.add_argument("--chemberta-anchors", type=Path, default=None,
                    help="path to phgdh_anchors.pt for chemberta reward")
    ap.add_argument("--reward-fn", default="qed_only", choices=["qed_only", "drugclip_phgdh", "vina_quick", "chemberta"])
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--steps", type=int, default=2000)
    ap.add_argument("--lr", type=float, default=1e-5)
    ap.add_argument("--beta-kl", type=float, default=0.1)
    ap.add_argument("--lambda-ent", type=float, default=0.01)
    ap.add_argument("--max-len", type=int, default=128)
    ap.add_argument("--temperature", type=float, default=1.0)
    ap.add_argument("--w-aff", type=float, default=1.0)
    ap.add_argument("--w-dl", type=float, default=0.3)
    ap.add_argument("--w-nov", type=float, default=0.3)
    ap.add_argument("--w-inv", type=float, default=1.0)
    ap.add_argument("--w-sa", type=float, default=0.1)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--save-every", type=int, default=200)
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    random.seed(args.seed); torch.manual_seed(args.seed)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[rl] device={device}", flush=True)

    if Chem is None:
        sys.exit("RDKit required for reward computation")
    if sf is None:
        sys.exit("selfies required for SELFIES↔SMILES")

    vocab_meta = json.loads(args.vocab.read_text())
    vocab = vocab_meta["vocab"]
    tok2i = {t: i for i, t in enumerate(vocab)}
    i2tok = {i: t for t, i in tok2i.items()}
    pad_id = tok2i.get(PAD, 0); bos_id = tok2i.get(START, 1); eos_id = tok2i.get(END, 2)

    # Build policy + prior with same arch (read config from sibling config.json)
    config_path = args.pretrain.parent / "config.json"
    cfg = json.loads(config_path.read_text())

    def make_model():
        m = SmallTransformer(
            vocab=cfg["vocab_size"], d_model=cfg["d_model"], n_heads=cfg["n_heads"],
            n_layers=cfg["n_layers"], ffn_dim=cfg["ffn_dim"],
            max_len=cfg.get("max_len", args.max_len), dropout=0.0,
        ).to(device)
        ck = torch.load(args.pretrain, map_location=device)
        m.load_state_dict(ck["model"])
        return m

    print("[rl] loading policy + prior", flush=True)
    policy = make_model()
    prior = make_model()
    for p in prior.parameters():
        p.requires_grad_(False)
    prior.eval()

    n_params = sum(p.numel() for p in policy.parameters() if p.requires_grad)
    print(f"[rl] trainable params={n_params:,}", flush=True)

    # Known actives FP for novelty
    known_fps = []
    if args.known_actives and args.known_actives.exists():
        for line in args.known_actives.open():
            s = line.strip().split()[0]
            mol = Chem.MolFromSmiles(s)
            if mol:
                known_fps.append(AllChem.GetMorganFingerprintAsBitVect(mol, 2, 2048))
        print(f"[rl] loaded {len(known_fps)} known-active fingerprints", flush=True)

    chemberta_scorer = None
    if args.reward_fn == "chemberta":
        anchors_path = args.chemberta_anchors or Path("/data/user/jakechen/aim4_clm/chemberta/phgdh_anchors.pt")
        if not anchors_path.exists():
            sys.exit(f"--reward-fn chemberta requires anchors at {anchors_path}")
        print(f"[rl] loading ChemBERTa scorer from {anchors_path}", flush=True)
        chemberta_scorer = ChemBERTaScorer(str(anchors_path), device=device)
        print(f"[rl] chemberta scorer ready, {chemberta_scorer.anchor_emb_n.shape[0]} anchors", flush=True)
    reward_fn = RewardFn(args, known_fps=known_fps, chemberta=chemberta_scorer)
    optim = torch.optim.AdamW(policy.parameters(), lr=args.lr)

    log_path = args.out / "rl_log.csv"
    with log_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["step", "reward_mean", "reward_max", "valid_rate", "novelty_mean",
                    "kl_to_prior", "entropy", "loss", "secs"])

        for step in range(args.steps):
            t0 = time.time()
            policy.train()

            # Sample from policy
            seq, log_probs = sample_with_log_probs(
                policy, args.max_len, cfg["vocab_size"], bos_id, eos_id, pad_id,
                args.batch, device, temperature=args.temperature,
            )
            # Decode to SMILES + compute rewards
            smiles_batch = decode_to_smiles(seq[:, 1:], i2tok, eos_id, pad_id)
            rewards = reward_fn(smiles_batch).to(device)

            # Forward through prior to compute KL on the same sequences
            with torch.no_grad():
                prior_logits = prior(seq[:, :-1])
            policy_logits = policy(seq[:, :-1])
            kl = kl_to_prior(policy_logits, prior_logits)

            # Entropy of policy distribution (averaged over valid tokens)
            mask = (seq[:, 1:] != pad_id).float()
            policy_dist = Categorical(logits=policy_logits)
            entropy = (policy_dist.entropy() * mask).sum() / mask.sum().clamp(min=1)

            # Policy gradient: -E[r * log_prob] (REINFORCE; PPO would clip ratio)
            # Sum log_probs along sequence dim, masked to valid tokens
            seq_log_prob = (log_probs * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)
            advantage = rewards - rewards.mean()  # baseline = batch mean
            pg_loss = -(advantage * seq_log_prob).mean()

            loss = pg_loss + args.beta_kl * kl - args.lambda_ent * entropy

            optim.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(policy.parameters(), 1.0)
            optim.step()

            # Stats
            valid = sum(1 for s in smiles_batch if s and Chem.MolFromSmiles(s) is not None)
            valid_rate = valid / max(1, len(smiles_batch))
            nov_vals = []
            if known_fps:
                for s in smiles_batch:
                    mol = Chem.MolFromSmiles(s) if s else None
                    if mol is None: continue
                    fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, 2048)
                    sims = DataStructs.BulkTanimotoSimilarity(fp, known_fps)
                    nov_vals.append(1.0 - (max(sims) if sims else 0.0))
            nov_mean = sum(nov_vals)/len(nov_vals) if nov_vals else 0.0

            dt = time.time() - t0
            w.writerow([step, f"{rewards.mean().item():.4f}", f"{rewards.max().item():.4f}",
                        f"{valid_rate:.4f}", f"{nov_mean:.4f}",
                        f"{kl.item():.4f}", f"{entropy.item():.4f}",
                        f"{loss.item():.4f}", f"{dt:.1f}"])
            f.flush()

            if step % 10 == 0:
                print(f"[rl] step={step} r_mean={rewards.mean():.3f} r_max={rewards.max():.3f} "
                      f"valid={valid_rate:.2%} nov={nov_mean:.3f} kl={kl:.3f} "
                      f"ent={entropy:.3f} loss={loss:.3f} ({dt:.1f}s)", flush=True)

            if step > 0 and step % args.save_every == 0:
                torch.save({"model": policy.state_dict(), "step": step,
                            "config": cfg}, args.out / f"rl_step_{step}.pt")

        # Final
        torch.save({"model": policy.state_dict(), "step": args.steps,
                    "config": cfg}, args.out / "rl_final.pt")
        print(f"[rl] done; final ckpt -> {args.out/'rl_final.pt'}", flush=True)


if __name__ == "__main__":
    main()
