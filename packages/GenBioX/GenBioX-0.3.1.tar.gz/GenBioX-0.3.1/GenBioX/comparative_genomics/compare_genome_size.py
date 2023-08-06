def compare_genome_size(genome1, genome2):
    """
    Compares the size of two genomes and reports the differences.

    Args:
        genome1 (str): The first genome sequence.
        genome2 (str): The second genome sequence.

    Returns:
        str: A string reporting the differences in genome size.
    """
    size1 = len(genome1)
    size2 = len(genome2)
    
    if size1 == size2:
        return "Genomes have the same size"
    elif size1 > size2:
        return "Genome 1 is larger by " + str(size1 - size2) + " nucleotides"
    else:
        return "Genome 2 is larger by " + str(size2 - size1) + " nucleotides"
