
from chembl_webresource_client.new_client import new_client
try:
    target = new_client.target
    search_res = target.search('PHGDH')
    if search_res:
        target_id = search_res[0]['target_chembl_id']
        print(f"Target Found: {target_id}")
        activities = new_client.activity
        res = activities.filter(target_chembl_id=target_id).get()
        print(f"Activities Found: {len(res)}")
    else:
        print("No target found.")
except Exception as e:
    print(f"Error: {e}")
