from Bio import pairwise2

def align(seq, ref_genome='ATCG...'):
    alignments = pairwise2.align.globalxx(ref_genome, seq)
    best_alignment = max(alignments, key=lambda x: x[2])
    return best_alignment
