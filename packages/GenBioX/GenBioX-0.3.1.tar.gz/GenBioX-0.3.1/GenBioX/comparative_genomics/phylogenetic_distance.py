def phylogenetic_distance(seq1, seq2):
    """
    Calculates the Jukes-Cantor distance between two DNA sequences.
    """
    p = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            p += 1

    p = float(p) / len(seq1)
    if p == 0:
        return 0
    else:
        return -0.75 * np.log(1 - (4 / 3) * p)

