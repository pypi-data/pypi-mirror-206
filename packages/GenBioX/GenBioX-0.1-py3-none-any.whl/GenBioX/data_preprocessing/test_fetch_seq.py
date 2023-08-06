from  fetch_seq import fetch_seq
from fasta_quality_check import fasta_quality_check

sequence = fetch_seq('nucleotide', 'NM_001109026.1')
print(sequence)

seq = fasta_quality_check(sequence)
print(seq)