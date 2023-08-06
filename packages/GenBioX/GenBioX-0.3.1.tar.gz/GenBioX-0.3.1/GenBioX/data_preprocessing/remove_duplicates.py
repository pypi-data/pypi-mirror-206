def remove_duplicates(sequences):
    """
    Identifies and removes duplicate reads from a list of FASTA sequences.
    Returns a list of unique sequences.
    """
    unique_sequences = []
    duplicate_count = 0
    for sequence in sequences:
        try:
            sequence_index = unique_sequences.index(sequence)
            duplicate_count += 1
        except ValueError:
            unique_sequences.append(sequence)
    print(f"Removed {duplicate_count} duplicate sequences.")
    return unique_sequences
