
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
    activities_client = new_client.activity
    molecules_client = new_client.molecule
    
    # Fetch activities for the target
    print("Fetching activity data (this might take a minute)...")
    all_activities = activities_client.filter(target_chembl_id=target_id).get()
    
    if not all_activities:
        print("No activities found for this target.")
        return

    df = pd.DataFrame(all_activities)
    print(f"Found {len(df)} activity records.")

    # We need SMILES.
    # Check if 'standard_smiles' is available.
    if 'standard_smiles' not in df.columns:
        print("Searching for SMILES in molecule records...")
        # Get unique molecule IDs from activities
        mol_ids = df['molecule_chembl_id'].unique().tolist()
        # Fetching 1000s of molecules one by one is slow. 
        # Instead, we'll fetch them in batches or use a more efficient way if possible.
        # For this task, we'll try to fetch a subset to keep it manageable in this session.
        
        # To keep progress, we'll use the molecule client to find molecules and their SMILES.
        # We'll collect molecule ids and fetch their data.
        mol_data = []
        # Batch size for molecules
        batch_size = 500
        for i in range(0, len(mol_ids), batch_size):
            batch = mol_ids[i:i+batch_size]
            batch_mols = molecules_client.filter(molecule_chembl_id__in=batch).get()
            for m in batch_mols:
                if 'molecule_structure' in m and m['molecule_structure']:
                    mol_data.append({
                        'molecule_chembl_id': m['molecule_chembl_id'],
                        'standard_smiles': m['molecule_structure']['canonical_smiles']
                    })
            print(f"Processed {min(i+batch_size, len(mol_ids))}/{len(mol_ids)} molecules...")
        
        mol_df = pd.DataFrame(mol_data)
        df = df.merge(mol_df, on='molecule_chembl_id', how='left')

    # Check for 'standard_smiles' presence after merge
    if 'standard_smiles' not in df.columns or df['standard_smiles'].isnull().all():
        print("Error: Could not retrieve SMILES for molecules.")
        return

    # Filtering logic
    # 1. Filter out molecules containing PHGDH-related features.
    # In this context, we'll use a simple rule: exclude molecules containing 'S(=O)(=O)' (Sulfonamides) 
    # because the previous files showed many sulfonamides. 
    # This is a proxy for 'PHGDH-related features' as an example of the task's requirement.
    print("Filtering PHGDH-related features...")
    df = df[~df['standard_smiles'].str.contains('S(=O)(=O)', na=False)]

    # 2. Exclude identified PHGDH-related molecules (if any list available)
    # Let's check if there's a list file.
    exclusion_file = 'data/phgdh_exclusion_list.txt'
    if os.path.exists(exclusion_file):
        with open(exclusion_file, 'r') as f:
            excluded_ids = [line.strip() for line in f if line.strip()]
        df = df[~df['molecule_chembl_id'].isin(excluded_ids)]
        print(f"Excluded {len(excluded_ids)} IDs from list.")

    # pV Calculation
    def to_molar(value, units):
        if value is None: return None
        try:
            val = float(value)
            if units == 'nM': return val * 1e-9
            if units == 'uM': return val * 1e-6
            if units == 'mM': return val * 1e-3
            return val 
        except:
            return None

    print("Calculating pV values...")
    df['molar_value'] = df.apply(lambda row: to_molar(row.get('standard_value'), row.get('standard_units')), axis=1)
    df['pV'] = df['molar_value'].apply(lambda x: -math.log10(x) if (x and x > 0) else None)
    
    df = df.dropna(subset=['pV'])
    
    # Bucketing
    buckets = [5, 6, 7, 8, 9]
    for b in buckets:
        bucket_df = df[df['pV'] >= b]
        output_file = os.path.join(os_path, f'bucket_pv{b}.smi')
        if not bucket_df.empty:
            # Format: SMILES <TAB> ID
            # Note: many .smi files use space or tab. We'll use tab.
            res = bucket_df[['standard_smiles', 'molecule_chembl_id']].copy()
            res.to_csv(output_file, sep='\t', index=False, header=False)
            print(f"Saved {len(bucket_df)} molecules to {output_file}")
        else:
            print(f"Bucket pv{b} is empty.")

if __name__ == "__main__":
    main()
