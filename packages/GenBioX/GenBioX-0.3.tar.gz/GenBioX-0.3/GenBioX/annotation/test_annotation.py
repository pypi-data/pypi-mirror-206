import annotation

# Extract annotations from GenBank file
annotations = annotation.extract_annotations("test_annotation2.gb")

# Filter annotations based on criteria
filter_dict = {"product": "Beta-lactamase"}
filtered_annotations = annotation.filter_annotations(annotations, filter_dict)

# Search annotations for a query
query = "aminoglycoside"
matched_annotations = annotation.search_annotations(annotations, query)

# Print results
print("Annotations:", annotations)
print("Filtered annotations:", filtered_annotations)
print("Matched annotations:", matched_annotations)
