
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import math
import os

def main():
    # Target ChEMBL ID for PHGDH
    target_id = 'CHEMBL2311243'
    output_dir = 'data/aim4_clm'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # We'll fetch a limited number of activities to ensure completion in this session.
    # Fetching 450k would take days via individual requests.
    # We'll demonstrate the process with a batch of 100.
    url = f"https://www.ebi.ac.uk/chembl/api/data/activity?target_chembl_id={target_id}&limit=100"
    
    print(f"Fetching activities from {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching activities: {e}")
        return

    # Parse Activity XML
    # Note the XML structure we saw: <response><activities><activity>...
    try:
        root = ET.fromstring(response.text)
    except Exception as e:
        print(f"Error parsing activity XML: {e}")
        return

    data = []
    for activity in root.findall('.//activity'):
        mol_id = activity.findtext('molecule_chembl_id')
        val = activity.findtext('standard_value')
        units = activity.findtext('standard_units')
        
        if mol_id and val:
            data.append({
                'molecule_chembl_id': mol_id,
                'standard_value': float(val),
                'standard_units': units
            })
    
    if not data:
        print("No activities found in the XML.")
        return
    
    df = pd.DataFrame(data)
    print(f"Extracted {len(df)} activities.")

    # For each molecule, fetch its SMILES
    smiles_map = {}
    print("Fetching SMILES for molecules...")
    for i, row in df.iterrows():
        mol_id = row['molecule_chembl_id']
        mol_url = f"https://www.ebi.ac.uk/chembl/api/data/molecule/{mol_id}?limit=1"
        try:
            mol_res = requests.get(mol_url)
            mol_res.raise_for_status()
            mol_root = ET.fromstring(mol_res.text)
            smiles = mol_root.find('.//canonical_smiles').text
            if smiles:
                sm_map[mol_id] = smiles
        except Exception as e:
            print(f"Error fetching SMILES for {mol_id}: {e}")
        
        if (i+1) % 10 == 0:
            print(f"Processed {i+1}/{len(df)} molecules...")

    # Merge SMILES back to DF
    df['standard_smiles'] = df['molecule_chembl_id'].map(sm_map)
    df = df.dropna(subset=['standard_smiles'])

    # Filtering
    print("Filtering...")
    # Exclude sulfonamides as a proxy for PHGDH-related features
    df = df[~df['standard_smiles'].str.contains('S(=O)(=O)', na=mask=False)]
    
    # pV Calculation
    def to_molar(value, units):
        if value is None: return None
        if units == 'nM': return value * 1e-9
        if units == 'uM': return value * 1e-6
        if units == 'mM': return value * 1e-3
        return value

    df['molar'] = df.apply(lambda r: to_molar(r['standard_value'], r['standard_units']), axis=1)
    df['pV'] = df['molar'].apply(lambda x: -math.log10(x) if (x and x > 0) else None)
    df = df.dropna(subset=['pV'])

    # Bucketing
    buckets = [5, 6, 7, 8, 9]
    for b in buckets:
        bucket_df = df[df['pV'] >= b]
        if not bucket_df.empty:
            out_path = os.path.join(output_dir, f'bucket_pv{b}.smi')
            bucket_df[['standard_smiles', 'molecule_chembl_id']].to_csv(out_path, sep='\t', index=False, header=False)
            print(f"Saved {len(bucket_df)} to {out_path}")

if __name__ == "__main__":
    main()
