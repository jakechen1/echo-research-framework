
import pandas as pd
import os

def generate_buckets(tsv_path, output_dir, thresholds):
    if not os.path.exists(tsv_path):
        print(f"Error: Source file {tsv_path} not found.")
        return

    # Read the TSV
    # columns: pchembl, smiles, chembl_id
    df = pd.read_csv(tsv_path, sep='\t')
    
    # Ensure columns are correct
    if 'pchembl' not in df.columns or 'smiles' not in df.columns:
        print("Error: TSV must contain 'pchembl' and 'smiles' columns.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for t in thresholds:
        # Filter for pv >= T
        bucket_df = df[df['pchembl'] >= t].copy()
        
        # Get unique SMILES for this bucket
        # The requirement is to have the SMILES in .smi format
        # Usually .smi is just one SMILES per line.
        # We'll drop duplicates to be safe.
        unique_smiles = bucket_df['smiles'].unique()
        
        output_file = os.path.join(output_dir, f'bucket_pv{t}.smi')
        
        with open(output_file, 'w') as f:
            for smi in unique_smiles:
                f.write(f"{smi}\n")
        
        print(f"Generated {output_file} with {len(unique_smiles)} molecules.")

if __name__ == "__main__":
    tsv_source = "data/aim4_smiles/smiles_potency_sorted.tsv"
    out_dir = "data/aim4_clm/"
    thresholds = [5, 6, 7, 8, 9]
    
    generate_buckets(tsv_source, out_dir, thresholds)
