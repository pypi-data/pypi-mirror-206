def differential_gene_expression_analysis(expression_data, group_labels):
    """
    Perform differential gene expression analysis using a statistical method such as t-test or ANOVA.

    Parameters:
    expression_data (pandas.DataFrame): a DataFrame containing gene expression data with samples as columns and genes as rows
    group_labels (list): a list containing group labels for each sample in the same order as the columns in expression_data

    Returns:
    pandas.DataFrame: a DataFrame containing the results of the differential gene expression analysis, including fold change, p-value, and adjusted p-value
    """

    # Import necessary libraries
    from scipy.stats import ttest_ind, f_oneway
    import pandas as pd
    import numpy as np
    from statsmodels.stats.multitest import multipletests

    # Create a dictionary to store results
    results = {'Gene': [], 'Fold Change': [], 'P-value': []}

    # Iterate over each gene in the expression data
    for gene in expression_data.index:

        # Get the expression values for this gene across all samples
        gene_expression = expression_data.loc[gene]

        # Split the expression values into groups based on the group labels
        groups = {}
        for i, label in enumerate(group_labels):
            if label not in groups:
                groups[label] = []
            groups[label].append(gene_expression[i])

        # Perform statistical test (e.g. t-test or ANOVA) to compare expression between groups
        # In this example, we use a two-sample t-test
        group1 = groups[group_labels[0]]
        group2 = groups[group_labels[1]]
        t_statistic, p_value = ttest_ind(group1, group2)

        # Calculate fold change between the two groups
        mean1 = np.mean(group1)
        mean2 = np.mean(group2)
        fold_change = mean2 / mean1

        # Add results to dictionary
        results['Gene'].append(gene)
        results['Fold Change'].append(fold_change)
        results['P-value'].append(p_value)

    # Convert results dictionary to a DataFrame
    results_df = pd.DataFrame(results)

    # Correct for multiple testing using a method such as Benjamini-Hochberg correction
    p_values = results_df['P-value'].values
    _, adj_p_values, _, _ = multipletests(p_values, method='fdr_bh')
    results_df['Adjusted P-value'] = adj_p_values

    return results_df
