def search_annotations(annotations, query):
    """
    Searches annotation information based on a user-defined query.

    Parameters:
    annotations (list): a list of dictionaries containing the annotation information
    query (str): the user-defined query

    Returns:
    list: a list of dictionaries containing the matching annotation information
    """
    try:
        matched_annotations = []
        for annotation in annotations:
            if query in str(annotation):
                matched_annotations.append(annotation)
        return matched_annotations
    except Exception as e:
        print(f"Error in search_annotations: {e}")
        return []