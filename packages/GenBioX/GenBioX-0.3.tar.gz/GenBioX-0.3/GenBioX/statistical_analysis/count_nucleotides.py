def count_nucleotides(seq):
    """
    Counts the number of A, C, G, and T/U nucleotides in a nucleotide sequence.

    Args:
    - seq (str): A string containing a nucleotide sequence.

    Returns:
    - dict: A dictionary with keys 'A', 'C', 'G', and 'T/U', and values representing the
      count of each nucleotide in the input sequence.
    """

    nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T/U': 0}

    for nucleotide in seq:
        try:
            nucleotide_counts[nucleotide.upper()] += 1
        except KeyError:
            print(f"Warning: Ignoring invalid nucleotide '{nucleotide}'")

    return nucleotide_counts

