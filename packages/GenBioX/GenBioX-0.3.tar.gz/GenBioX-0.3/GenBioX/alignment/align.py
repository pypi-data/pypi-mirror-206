from Bio import pairwise2

def align(seq, ref, algorithm='global'):
    """
    Aligns a given sequence to a reference genome using a specified alignment algorithm.
    
    Args:
        seq (str): The sequence to be aligned.
        ref (str): The reference genome sequence to align against.
        algorithm (str): The alignment algorithm to use (default is 'global').
        
    Returns:
        str: The aligned sequence.
    """
    if algorithm == 'global':
        alignment = pairwise2.align.globalxx(seq, ref)
    elif algorithm == 'local':
        alignment = pairwise2.align.localxx(seq, ref)
    else:
        raise ValueError('Invalid algorithm specified. Supported algorithms are "global" and "local".')
    
    aligned_seq = alignment[0].replace('-', '')
    
    return aligned_seq
