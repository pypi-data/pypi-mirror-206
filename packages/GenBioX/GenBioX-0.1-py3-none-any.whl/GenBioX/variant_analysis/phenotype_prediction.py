import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def phenotype_prediction(variants, phenotypes):
    # Load variant and phenotype data into pandas dataframes
    variants_df = pd.read_csv(variants)
    phenotypes_df = pd.read_csv(phenotypes)
    
    # Merge variant and phenotype dataframes on common columns
    merged_df = pd.merge(variants_df, phenotypes_df, on='sample_id')
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        merged_df.drop(columns=['sample_id', 'phenotype']),
        merged_df['phenotype'],
        test_size=0.2,
        random_state=42
    )
    
    # Train random forest classifier on training data
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Evaluate classifier performance on testing data
    accuracy = clf.score(X_test, y_test)
    
    return accuracy
