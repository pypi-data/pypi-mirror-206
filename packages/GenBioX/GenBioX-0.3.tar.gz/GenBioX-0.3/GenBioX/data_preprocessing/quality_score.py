import math

def quality_score(sequence):
    """
    Calculates the Phred quality score for each base in a FASTA sequence.
    Returns a list of quality scores for each base.
    """
    qs = []
    for base in sequence:
        try:
            # Calculate the estimated probability of an incorrect base call
            error_prob = 10 ** (-ord(base) / 10)
            # Calculate the Phred quality score using the estimated error probability
            phred_score = -10 * math.log10(error_prob)
            qs.append(phred_score)
        except ValueError:
            # If the character is not recognized as a valid base, assign a quality score of 0
            qs.append(0)
    return qs
