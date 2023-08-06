import pandas as pd


def gene_expression_correlation(expression_data, clinical_data):
    """
    Calculates the correlation between gene expression levels and clinical variables.

    Parameters:
    expression_data (pandas.DataFrame): A dataframe containing gene expression levels.
    clinical_data (pandas.DataFrame): A dataframe containing clinical variables.

    Returns:
    pandas.DataFrame: A dataframe containing the correlation coefficients between each gene and each clinical variable.
    """
    # Merge expression and clinical data on a shared column, such as sample ID or patient ID
    merged_data = pd.merge(expression_data, clinical_data, on='sample_id')

    # Calculate Pearson correlation coefficient for each gene and each clinical variable
    correlation_matrix = merged_data.corr(method='pearson')

    return correlation_matrix
