def evaluate_alignment_quality(aln):
    num_seqs = len(aln)
    aln_length = aln.get_alignment_length()
    num_gaps = sum(seq.seq.count('-') for seq in aln)
    num_matches = 0
    num_mismatches = 0
    for i in range(aln_length):
        column = aln[:, i]
        if len(set(column)) > 1:
            num_mismatches += 1
        else:
            num_matches += 1
    coverage = (num_matches + num_gaps) / (num_seqs * aln_length)
    accuracy = num_matches / (num_matches + num_mismatches)
    gap_distribution = num_gaps / aln_length

    quality_metrics = {'coverage': coverage,
                       'accuracy': accuracy,
                       'gap_distribution': gap_distribution}

    return quality_metrics
