# Task 4.4 — CLM incremental fine-tune plan

Per Fan Li et al. (Nat Commun 2026-04-11, s41467-026-71591-w):

1. Pretrain LSTM on ~450K ChEMBL bioactives (excluding PHGDH target ligands)
2. Incremental fine-tune steps:
   - step 1: all 1011 PHGDH molecules (pv >= 5)
   - step 2: pv >= 6 subset (~463 molecules)
   - step 3: pv >= 7 subset (20 molecules — our Top-20)
   - step 4: pv >= 8 subset
   - step 5: pv >= 9 subset (most potent known)
3. Generate 10K candidates, rank by perplexity (low perplexity = predicted potent)
4. Filter top 500 → Task 4.5 Vina rerank into 6RIH K4T pocket

## Data prepared in this dir
- bucket_pv5.smi through bucket_pv9.smi — ready for tokenization

## Next step requires
- PyTorch + torch-text OR RDKit-based SMILES tokenizer on L0
- ChEMBL download: ~450K bioactives excluding PHGDH target (UniProt O43175)
- Run LSTM pretrain on L0 GPU (~4-6 hours on M4 Pro)

## Estimated time
- Data prep (done here): minutes
- LSTM pretrain: 4-6 hours on L0
- Fine-tune steps 1-5: 30 min each (~2.5 hours)
- Generation + ranking: 30 min
- Total: ~8 hours of overnight L0 GPU time

Start the training by running the PyTorch pipeline on L0 (to be written
as separate script once PyTorch env confirmed).
