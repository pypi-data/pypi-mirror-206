def gene_expression_normalization(data, method='quantile'):
    """
    Normalize gene expression data to remove technical variations and biases
    
    Args:
    data (pandas.DataFrame): gene expression data, where rows are samples and columns are genes
    method (str): normalization method, default is 'quantile'
        'quantile': normalize each sample to the same distribution of expression values using quantiles
        'zscore': normalize each gene to have a mean of 0 and standard deviation of 1 across samples
    
    Returns:
    pandas.DataFrame: normalized gene expression data
    
    """
    
    if method == 'quantile':
        # normalize each sample to the same distribution of expression values using quantiles
        data = data.rank(pct=True)
    
    elif method == 'zscore':
        # normalize each gene to have a mean of 0 and standard deviation of 1 across samples
        data = (data - data.mean()) / data.std()
    
    return data
