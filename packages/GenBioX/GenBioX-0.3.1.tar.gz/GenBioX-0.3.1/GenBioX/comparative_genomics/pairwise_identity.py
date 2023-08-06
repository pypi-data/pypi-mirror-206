def pairwise_identity(seq1, seq2, method='global'):
    """
    Calculates the pairwise identity between two sequences.

    Args:
        seq1 (str): First sequence.
        seq2 (str): Second sequence.
        method (str): Method to use for identity calculation. Can be 'global' (default) for global alignment or 'local' for local alignment.

    Returns:
        float: Pairwise identity between the two sequences as a percentage.
    """

    # Import pairwise2 function from Biopython
    from Bio import pairwise2

    # Set alignment parameters
    if method == 'global':
        aligner = pairwise2.align.globalxx
    elif method == 'local':
        aligner = pairwise2.align.localxx
    else:
        raise ValueError('Invalid method specified. Must be "global" or "local".')

    # Perform sequence alignment
    alignments = aligner(seq1, seq2)

    # Get best alignment and calculate identity
    best_alignment = alignments[0]
    identity = best_alignment[2] / len(seq1)

    # Convert identity to percentage
    identity_percent = identity * 100

    return identity_percent
