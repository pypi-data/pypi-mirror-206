def count_nucleotides(sequence):
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}
    valid_nucleotides = ["A", "C", "G", "T"]
    for nucleotide in sequence:
        if nucleotide in valid_nucleotides:
            counts[nucleotide] += 1
    return counts
