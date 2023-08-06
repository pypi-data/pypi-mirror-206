def calculate_gc_content(seq):
    """Calculates the GC content of a nucleotide sequence."""
    try:
        gc_count = seq.count('G') + seq.count('C')
        gc_content = float(gc_count) / len(seq) * 100
        return gc_content
    except ZeroDivisionError:
        print("Error: sequence length is zero.")

