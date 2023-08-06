def trim_adapters(sequence, adapter='AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC'):
    """
    Trims adapter sequences from the 3' end of a FASTA sequence.
    Returns the trimmed sequence.
    """
    try:
        # Find the index of the adapter sequence in the reverse complement of the sequence
        rev_comp = sequence[::-1].translate(str.maketrans('ATCG', 'TAGC'))
        adapter_idx = rev_comp.find(adapter[::-1])
        if adapter_idx == -1:
            # If adapter sequence is not found, return the original sequence
            return sequence
        else:
            # Trim the adapter sequence from the 3' end of the sequence
            trimmed_sequence = sequence[:-adapter_idx-1]
            return trimmed_sequence
    except TypeError:
        # If the input sequence is not a string or is empty, return None
        return None
