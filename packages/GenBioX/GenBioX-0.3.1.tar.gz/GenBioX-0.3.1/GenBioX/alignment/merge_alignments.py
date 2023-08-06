from Bio.Align import MultipleSeqAlignment

def merge_alignments(aln1, aln2):
    # Check that the alignments have the same length
    if len(aln1) != len(aln2):
        raise ValueError("Alignments have different lengths")

    # Merge the sequences and annotations
    merged_seqs = []
    merged_annotations = []
    for i in range(len(aln1)):
        seq1 = aln1[i]
        seq2 = aln2[i]
        if seq1.id != seq2.id:
            raise ValueError("Sequences have different IDs")
        merged_seq = seq1 + seq2
        merged_seqs.append(merged_seq)
        merged_annotations.append(seq1.annotations)

    # Create a new alignment object with the merged sequences and annotations
    merged_aln = MultipleSeqAlignment(merged_seqs)
    merged_aln.annotations = merged_annotations

    return merged_aln
