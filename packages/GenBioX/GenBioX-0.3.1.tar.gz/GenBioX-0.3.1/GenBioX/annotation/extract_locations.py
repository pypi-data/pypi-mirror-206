import pandas as pd
from Bio import SeqIO

def extract_locations(genbank_file):
    annotations = []
    for record in SeqIO.parse(genbank_file, 'genbank'):
        for feature in record.features:
            if feature.type == 'gene':
                gene_name = feature.qualifiers.get('gene', [''])[0]
                location = str(feature.location)
                annotations.append({'gene_name': gene_name, 'location': location})
    return pd.DataFrame(annotations)

