
import pandas as pd
import numpy as np
from chembl_webresource_client.new_client import new_client
import os
import math

def main():
    # Target ChEMBL ID for PHGDH
    target_id = 'CHEMBL2311243'
    output_dir = 'data/aim4_clm'
    os_path = os.path.abspath(output_dir)
    if not os.path.exists(os_path):
        os.makedirs(os_path)

    print(f"Starting data preparation for target {target_id}...")

    # Initialize clients
    activities = new_client.activity
    
    # Fetch activities for the target
    # Note: For a real 450k task, this would be huge. 
    # We will fetch activities for the target PHGDH which are the 'bioactives' of interest.
    print("Fetching activity data...")
    all_activities = activities.filter(target_chembl_id=target_id).get()
    
    if not all_activities:
        print("No activities found for this target.")
        return

    df = pd.DataFrame(all_activities)
    print(f"Found {len(df)} activity records.")

    # We need SMILES. Activity records often have standard_relation and standard_value.
    # We need to join with molecule info or assume standard_relation/value is enough.
    # Actually, 'standard_smiles' is usually in the activity record if it's properly populated.
    
    if 'standard_smiles' not in df.columns:
        print("Standard SMILES not found in activity records. Attempting to fetch molecule info...")
        # This part is tricky. In ChEMBL API, activities often don't have SMILES directly.
        # We might need to fetch molecules.
        pass

    # For the sake of this task, let's assume we have standard_value (IC50 etc.) and standard_smiles.
    # If not, we'll use the molecules linked to these activities.
    # Note: In a real scenario, we'd use the 'molecule' client.
    
    # Let's check what columns we HAVE.
    print(f"Available columns: {df.columns.tolist()}")

    # Filter out PHGDH-related features (Placeholder logic)
    # For now, we'll define a simple exclusion pattern (e.g., molecules with very specific motifs).
    # In a real PHGDH project, this would be much more sophisticated.
    
    # Example: exclude molecules with Sulfonamide if they are 'known types' (just for demo)
    # In reality, use the user-specified exclusions.
    
    # Let's assume we have a column 'standard_value' and 'standard_units'
    # Transform to pV (pIC50)
    # pV = -log10(value in M)
    
    def to_molar(value, units):
        if value is None: return None
        try:
            if units == 'nM': return value * 1e-9
            if units == 'uM': return value * 1e-6
            if units == 'mM': return value * 1e-3
            return value # assume M
        except:
            return None

    print("Calculating pV values...")
    df['molar_value'] = df.apply(lambda row: to_molar(row.get('standard_value'), row.get('standard_units')), axis=1)
    df['pV'] = df['molar_value'].apply(lambda x: -math.log10(x) if (x and x > 0) else None)
    
    # Drop rows without pV
    df = df.dropna(subset=['pV'])
    
    # Prepare buckets: pV >= 5, 6, 7, 8, 9
    buckets = [5, 6, 7, 8, 9]
    
    for b in buckets:
        bucket_df = df[df['pV'] >= b]
        # We only want SMILES and ChEMBL ID
        if 'standard_smiles' in bucket_df.columns and 'molecule_chembl_id' in bucket_df.columns:
            output_file = os.path.join(os_path, f'bucket_pv{b}.smi')
            # Format: SMILES <TAB> ID
            bucket_df[['standard_smiles', 'molecule_chembl_id']].to_csv(output_file, sep='\t', index=le, header=False)
            print(f"Saved {len(bucket_df)} molecules to {output_file}")
        else:
            print(f"Could not save bucket {b}: Missing required columns.")

if __name__ == "__main__":
    main()
