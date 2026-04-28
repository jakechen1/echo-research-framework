# Bioactive corpora

| Source | File | Count | Use |
|---|---|---|---|
| ChEMBL 35 | bioactives.smi | 1,091,136 | iter 2 / iter 4 pretrain (current) |
| BindingDB All 202604 | bindingdb_bioactives.smi | 1,177,443 | merged for iter 5+ |
| ChEMBL ∪ BindingDB (deduped) | bioactives_merged.smi | 1,672,507 | iter 5+ pretrain corpus |

## Filters
- pchembl_value ≥ 5 (~10 µM threshold)
- target ≠ CHEMBL2311243 (PHGDH itself)
- length(canonical_smiles) ∈ [5, 200]
- no salt fragments ("." in SMILES rejected)
- 5 ≤ heavy atoms ≤ 80
- canonicalized via RDKit, deduplicated by canonical SMILES

## File locations on Cheaha
- /data/user/jakechen/aim4_clm/bioactives.smi
- /data/user/jakechen/aim4_clm/bindingdb/bindingdb_bioactives.smi
- /data/user/jakechen/aim4_clm/bioactives_merged.smi
