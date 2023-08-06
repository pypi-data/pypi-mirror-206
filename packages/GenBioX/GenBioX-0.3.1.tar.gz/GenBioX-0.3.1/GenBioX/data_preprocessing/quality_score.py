def quality_score(seq):
    """
    Calculates the Phred quality score for each base in a FASTA sequence.
    Returns a list of quality scores for each base.
    """
    qualities = []
    for base in seq:
        if base in ["A", "T", "C", "G"]:
            quality = ord(base) - 33
            qualities.append(quality)
        else:
            qualities.append(0)
    return qualities
