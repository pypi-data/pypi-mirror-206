from Bio import pairwise2
from Bio import SeqIO

def pairwise_alignment(seq1_file, seq2_file, gap_penalty=-10, match_score=5, mismatch_penalty=-4):
    # Read in the sequences from the files
    seq1 = SeqIO.read(seq1_file, "fasta")
    seq2 = SeqIO.read(seq2_file, "fasta")
    
    # Perform pairwise alignment using Needleman-Wunsch algorithm
    alignments = pairwise2.align.globalms(seq1.seq, seq2.seq, match_score, mismatch_penalty, gap_penalty, gap_penalty)
    
    # Print the alignment
    for alignment in alignments:
        print(pairwise2.format_alignment(*alignment))
