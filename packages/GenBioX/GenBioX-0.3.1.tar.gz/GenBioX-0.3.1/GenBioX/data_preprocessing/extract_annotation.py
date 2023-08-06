from Bio import SeqIO

def extract_annotations(genbank_file):
    """
    Extracts annotation information from a genbank file.

    Parameters:
    genbank_file (str): path to the genbank file

    Returns:
    list: a list of dictionaries containing the extracted annotation information
    """
    try:
        annotations = []
        for record in SeqIO.parse(genbank_file, "genbank"):
            for feature in record.features:
                if feature.type == "CDS":
                    annotation_dict = {}
                    if "gene" in feature.qualifiers:
                        annotation_dict["gene"] = feature.qualifiers["gene"][0]
                    if "product" in feature.qualifiers:
                        annotation_dict["product"] = feature.qualifiers["product"][0]
                    if "db_xref" in feature.qualifiers:
                        for db_xref in feature.qualifiers["db_xref"]:
                            if db_xref.startswith("ARO:"):
                                annotation_dict["aro_accession"] = db_xref
                                break
                    annotations.append(annotation_dict)
        return annotations
    except Exception as e:
        print(f"Error in extract_annotations: {e}")
        return []