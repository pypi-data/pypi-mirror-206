def search_annotations(annotations, query):
    filtered_annotations = []
    for feature_props in annotations:
        if 'product' in feature_props and query.lower() in feature_props['product'].lower():
            filtered_annotations.append(feature_props)
    return filtered_annotations
