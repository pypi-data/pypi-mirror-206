import numpy as np 

def gene_expression_quantification(counts_matrix, lengths):
    """
    Quantifies gene expression levels using RPKM method.
    
    Args:
    counts_matrix (numpy array): Matrix of read counts, where each row represents a gene and each column represents a sample.
    lengths (numpy array): Vector of gene lengths.
    
    Returns:
    numpy array: Matrix of RPKM values, where each row represents a gene and each column represents a sample.
    """
    # Calculate the total number of reads in each sample
    total_reads = np.sum(counts_matrix, axis=0)
    
    # Calculate the read density for each gene
    read_density = counts_matrix / lengths.reshape(-1, 1)
    
    # Calculate the total number of reads per kilobase for each sample
    rpkm = read_density / (total_reads / 10**6)
    
    return rpkm
