def get_group_labels(data):
    """
    Get group labels from gene expression data frame
    
    Args:
    data (pandas.DataFrame): gene expression data frame, where rows are genes and columns are samples
    
    Returns:
    list: a list containing group labels for each sample in the same order as the columns in data
    """
    # Get the column names from the data frame
    columns = data.columns.tolist()

    # Remove the 'GENE' and 'NAME' columns
    columns.remove('GENE')
    columns.remove('NAME')

    # Separate the remaining columns into groups based on their prefix (i.e. the first character of their name)
    groups = set()
    for col in columns:
        group = col[0]
        groups.add(group)

    # Create a dictionary to store the group labels
    group_labels = {}
    for group in groups:
        group_columns = [col for col in columns if col.startswith(group)]
        for col in group_columns:
            group_labels[col] = group

    # Create a list of group labels in the same order as the columns in the data frame
    labels = [group_labels[col] for col in columns]

    return labels
