def fasta_quality_check(sequences, min_length=50, max_length=1000000):
    """
    Filters sequences by length and removes any sequence with invalid characters.
    Returns a dictionary of filtered sequences.

    Args:
        sequences (dict): A dictionary of sequence IDs and their corresponding sequences.
        min_length (int): Minimum length of sequence (default 50).
        max_length (int): Maximum length of sequence (default 1000000).

    Returns:
        dict: A dictionary with sequence IDs as keys and filtered sequences as values.
    """

    filtered_sequences = {}
    valid_chars = set('ATCGatcgNn')

    for seq_id, seq in sequences.items():
        # Filter out sequences based on length
        if len(seq) < min_length or len(seq) > max_length:
            continue

        # Filter out sequences with invalid characters
        if not all(c in valid_chars for c in seq):
            continue

        filtered_sequences[seq_id] = seq

    return filtered_sequences
