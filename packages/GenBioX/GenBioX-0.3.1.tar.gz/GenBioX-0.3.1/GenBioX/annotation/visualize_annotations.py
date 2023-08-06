from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def visualize_annotations(gb_file):
    # read the genbank file and extract the sequence
    record = SeqIO.read(gb_file, 'genbank')
    seq_len = len(record.seq)

    # create a figure and axis
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, polar=True)

    # iterate over the features and add rectangles to the axis
    for feature in record.features:
        if feature.type == 'gene':
            start, end = feature.location.start.position, feature.location.end.position
            if start > end:
                start, end = end, start
            ax.add_patch(Rectangle((start/seq_len*2*np.pi, 0.35), (end-start)/seq_len*2*np.pi, 0.3, facecolor='orange', alpha=0.5))
    
    # set the axis limits and tick labels
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xticks(np.linspace(0, 2*np.pi, 12, endpoint=False))
    ax.set_xticklabels([f'{i*30}°' for i in range(12)])

    # show the plot
    plt.show()

