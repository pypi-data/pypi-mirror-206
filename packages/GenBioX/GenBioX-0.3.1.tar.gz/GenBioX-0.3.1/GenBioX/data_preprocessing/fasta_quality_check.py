def fasta_quality_check(nucleotides_list, quality_scores=None, min_quality_score=20):
    results = {}
    
    for i, nucleotides in enumerate(nucleotides_list):
        seq_id = f'Sequence_{i+1}'
        # Calculate length of sequence
        seq_length = len(nucleotides)
        # Calculate nucleotide counts
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for nt in nucleotides:
            counts[nt] += 1
        
        # Calculate GC content
        gc_content = (counts['G'] + counts['C']) / sum(counts.values())

        # Check quality scores if available
        if quality_scores:
            scores = quality_scores[i]
            if any(int(x) < min_quality_score for x in scores.split()):
                results[seq_id] = 'Sequence has low quality'
                continue
        
        # Add results to dictionary
        results[seq_id] = {
            'length': seq_length,
            'nucleotide_counts': counts,
            'GC_content': gc_content,
            'status': 'Passes quality check'
        }
        
    return results
