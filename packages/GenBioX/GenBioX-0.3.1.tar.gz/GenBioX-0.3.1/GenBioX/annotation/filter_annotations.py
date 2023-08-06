def filter_annotations(annotations, filter_dict):
    filtered_annotations = []
    for ann in annotations:
        if all(ann.get(prop) == value for prop, value in filter_dict.items()):
            filtered_annotations.append(ann)
    return filtered_annotations
