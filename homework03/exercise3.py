import json
import xmltodict

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
  
root = {}     
root['data'] = data

# writes the dictionary into XML
with open('proteins.xml', 'w') as o:
    o.write(xmltodict.unparse(root, pretty=True))
     
     
    
