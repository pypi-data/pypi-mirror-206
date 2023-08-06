def reverse_complement(seq):
    """
    Generates the reverse complement of a nucleotide sequence.
    
    Args:
    - seq (str): A string containing a nucleotide sequence.
    
    Returns:
    - str: The reverse complement of the input sequence.
    """
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_seq = seq[::-1]
    reverse_complement_seq = ''
    for nucleotide in reverse_seq:
        if nucleotide in complement:
            reverse_complement_seq += complement[nucleotide]
        else:
            reverse_complement_seq += nucleotide
    return reverse_complement_seq
