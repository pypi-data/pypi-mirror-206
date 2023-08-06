def filter_annotations(annotations, filter_dict):
    """
    Filters annotation information based on user-defined criteria.

    Parameters:
    annotations (list): a list of dictionaries containing the annotation information
    filter_dict (dict): a dictionary containing the filter criteria

    Returns:
    list: a list of dictionaries containing the filtered annotation information
    """
    try:
        filtered_annotations = []
        for annotation in annotations:
            if all(key in annotation and annotation[key] == value for key, value in filter_dict.items()):
                filtered_annotations.append(annotation)
        return filtered_annotations
    except Exception as e:
        print(f"Error in filter_annotations: {e}")
        return []