from Bio.Seq import Seq

def translate(nucleotides_list):
    protein_sequences = []
    for nucleotides in nucleotides_list:
        dna_sequence = Seq(''.join(nucleotides))
        protein_sequence = dna_sequence.translate()
        protein_sequences.append(str(protein_sequence))
    return protein_sequences
