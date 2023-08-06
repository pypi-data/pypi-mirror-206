import os
import sys
sys.path.append("/Users/li/Desktop/ResistomeX/ResistomeX/data_preprocessing")

import fasta_quality_check
import fasta



# Load the test FASTA file
sequences = fasta.read_fasta("test.fasta.txt")

# Print the sequences
for seq_id, seq in sequences.items():
    print(seq_id, seq)
