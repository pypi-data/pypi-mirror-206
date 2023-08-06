def trim_adapters(seq_list, adapter):
    """
    Removes adapter sequences from the 3' end of the nucleotide sequence(s) in seq_list.
    """
    trimmed_seqs = []
    for seq in seq_list:
        index = seq.rfind(adapter)
        if index != -1:
            trimmed_seqs.append(seq[:index])
        else:
            trimmed_seqs.append(seq)
    return trimmed_seqs
