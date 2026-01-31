import json
import csv

# this reads json into a python dictionary
with open('hw_input.json', 'r') as f:
    bio_data = json.load(f)

# this reads my python dictionary into a csv file
with open('proteins.csv', 'w') as o:
    writer = csv.writer(o)
    # this manually write headers as flat row names
    header = ['primaryAccession',
              'proteinName',
              'geneName',
              'organism_scientificName',
              'sequence_length',
              'sequence_mass',
              'function']
    writer.writerow(header)
    # this writes the row data, and extracts the nested values
    for protein in bio_data['protein_list']:
        row = [protein['primaryAccession'],
               protein['proteinName'],
               protein['geneName'],
               protein['organism']['scientificName'],
               protein['sequence']['length'],
               protein['sequence']['mass'],
               protein['function']]
        writer.writerow(row)
