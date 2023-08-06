import pandas as pd

def read_gene_expression_file(file_path):
    """
    Read gene expression data from file and convert it into a pandas DataFrame
    
    Args:
    file_path (str): path to the gene expression file
    
    Returns:
    pandas.DataFrame: gene expression data in a DataFrame format
    """
    # Check the file extension to determine the file type
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.txt'):
        df = pd.read_table(file_path)
    else:
        raise ValueError("File format not supported. Please provide a CSV or TXT file.")
    
    return df

