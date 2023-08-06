import numpy as np

def phylogenetic_distance(genome1, genome2):
    # Define nucleotide alphabet and transition matrix
    nucleotides = ['A', 'C', 'G', 'T']
    trans_matrix = np.array([[0.25, 0.25, 0.25, 0.25],
                             [0.25, 0.25, 0.25, 0.25],
                             [0.25, 0.25, 0.25, 0.25],
                             [0.25, 0.25, 0.25, 0.25]])

    # Convert genome sequences to arrays of integers (0-3)
    seq1 = np.array([nucleotides.index(nuc) for nuc in genome1])
    seq2 = np.array([nucleotides.index(nuc) for nuc in genome2])

    # Calculate proportion of nucleotide differences
    num_diff = np.sum(seq1 != seq2)
    prop_diff = num_diff / len(seq1)

    # Calculate Jukes-Cantor distance
    if prop_diff == 0:
        distance = 0
    else:
        distance = -(3/4)*np.log(1 - (4/3)*prop_diff)

    return distance
