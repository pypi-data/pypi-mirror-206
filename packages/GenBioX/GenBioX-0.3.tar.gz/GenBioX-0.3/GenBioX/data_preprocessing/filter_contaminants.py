def filter_contaminants(sequences, contaminants):
    """
    Identifies and removes reads that match known contaminant sequences from a list of FASTA sequences.
    Returns a list of non-contaminant sequences.
    """
    non_contaminant_sequences = []
    contaminant_count = 0
    for sequence in sequences:
        try:
            if any(contaminant in sequence for contaminant in contaminants):
                contaminant_count += 1
            else:
                non_contaminant_sequences.append(sequence)
        except TypeError:
            # If the input sequence is not a string or is empty, skip it
            pass
    print(f"Removed {contaminant_count} contaminant sequences.")
    return non_contaminant_sequences
