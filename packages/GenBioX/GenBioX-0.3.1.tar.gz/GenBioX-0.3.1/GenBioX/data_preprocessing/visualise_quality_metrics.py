import matplotlib.pyplot as plt
import numpy as np

def visualise_quality_metrics(sequences, quality_scores):
    """
    Generates plots and summary statistics to assess the quality of sequencing data.
    Plots include per-base quality scores and read length distributions.
    """
    # Calculate per-base quality score statistics
    mean_quality_scores = np.mean(quality_scores, axis=0)
    min_quality_scores = np.min(quality_scores, axis=0)
    max_quality_scores = np.max(quality_scores, axis=0)
    # Plot per-base quality scores
    fig, ax = plt.subplots()
    ax.plot(mean_quality_scores, label='Mean Quality Score')
    ax.plot(min_quality_scores, label='Min Quality Score')
    ax.plot(max_quality_scores, label='Max Quality Score')
    ax.set_xlabel('Base Position')
    ax.set_ylabel('Quality Score')
    ax.set_title('Per-Base Quality Scores')
    ax.legend()
    plt.show()
    # Calculate read length statistics
    read_lengths = [len(sequence) for sequence in sequences]
    mean_read_length = np.mean(read_lengths)
    median_read_length = np.median(read_lengths)
    # Plot read length distribution
    fig, ax = plt.subplots()
    ax.hist(read_lengths, bins=50)
    ax.axvline(x=mean_read_length, color='r', linestyle='--', label=f'Mean = {mean_read_length:.1f}')
    ax.axvline(x=median_read_length, color='g', linestyle='--', label=f'Median = {median_read_length:.1f}')
    ax.set_xlabel('Read Length')
    ax.set_ylabel('Count')
    ax.set_title('Read Length Distribution')
    ax.legend()
    plt.show()
    # Print summary statistics
    print(f"Number of reads: {len(sequences)}")
    print(f"Mean read length: {mean_read_length:.1f}")
    print(f"Median read length: {median_read_length:.1f}")
