import yaml
import json

# this reads json into a python dictionary
with open('hw_input.json', 'r') as f:
    bio_data = json.load(f)

data = {}
data['protein_entries'] = []

# this builds the dictionary by iterating through each protein in the JSON
for protein in bio_data['protein_list']:
    protein_entry ={
        "primaryAccession": protein["primaryAccession"],
        "organism": protein["organism"],
        "proteinName": protein["proteinName"],
        "sequence": protein["sequence"], 
        "geneName": protein["geneName"],    
        "function": protein["function"]
    }
    data['protein_entries'].append(protein_entry)

# writes the python dictionary into YAML
with open('proteins.yaml', 'w') as o:
   yaml.dump(data, o, sort_keys = False, explicit_start = True, explicit_end = True)
