def filter_reads(quality_scores, min_avg_score=20, max_low_quality_bases=5):
    """
    Filters out reads with low overall quality scores or too many low quality bases.
    Returns True if the read passes the quality filter, False otherwise.
    """
    try:
        # Calculate the average quality score for the read
        avg_score = sum(quality_scores) / len(quality_scores)
        # Count the number of bases with quality scores below a threshold
        low_quality_bases = sum(score < min_avg_score for score in quality_scores)
        # Return True if the read passes the quality filter, False otherwise
        return avg_score >= min_avg_score and low_quality_bases <= max_low_quality_bases
    except ZeroDivisionError:
        # If the length of quality_scores is zero, return False
        return False
