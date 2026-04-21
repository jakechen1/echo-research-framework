
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import math
import os

def main():
    # Target ChEMBL ID for PHGDH
    target_id = 'CHEMBL2311243'
    output_dir = 'data/aim4_clm'
    if not os.path_exists(output_dir):
        os.makedirs(output_dir)
    
    url = f"https://www.ebi.ac.uk/chembl/api/data/activity?target_chembl_id={target_id}&limit=50"
    
    print(f"Fetching activities from {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching activities: {e}")
        return

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

    smiles_map = {}
    print("Fetching SMILES for molecules...")
    for i, row in df.iterrows():
        mol_id = row['molecule_chembl_id']
        mol_url = f"https://www.ebi.ac.uk/chembl/api/data/molecule/{mol_id}?limit=1"
        try:
            mol_res = requests.get(mol_url)
            mol_res.raise_for_status()
            mol_root = ET.fromstring(mol_res.text)
            smiles_elem = mol_root.find('.//canonical_smiles')
            if smiles_elem is not None:
                smiles_map[mol_id] = smiles_elem.text
        except Exception as e:
            pass
        
        if (i+1) % 10 == 0:
            print(f"Processed {i+1}/{len(df)} molecules...")

    df['standard_smiles'] = df['molecule_chembl_id'].map(sm__map) # typo here
    # ...
