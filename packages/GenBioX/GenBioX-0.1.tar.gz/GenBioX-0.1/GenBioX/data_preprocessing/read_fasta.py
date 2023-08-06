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


    return sequences



