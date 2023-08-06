import sys
sys.path.append("/path/to/Users/li/Desktop/ResistomeX")

import fasta_quality_check

def read_fasta(filename):
    """
    Reads in a FASTA file and returns a dictionary of sequence IDs and their corresponding sequences.

    Args:
        filename (str): Name of the input FASTA file.

    Returns:
        dict: A dictionary with sequence IDs as keys and sequences as values.
    """

    sequences = {}
    current_sequence = ''

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()

            if line.startswith('>'):
                # > indicates Start of a new sequence
                current_sequence = line[1:]
                sequences[current_sequence] = ''
            else:
                sequences[current_sequence] += line

    # Run quality control check
    fasta_quality_check.fasta_quality_check(sequences)


    return sequences



