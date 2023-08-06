def identify_conserved_regions(genomes):
    """
    Identifies conserved regions between two or more genomes
    
    Parameters:
    genomes (list): List of genome sequences in string format
    
    Returns:
    conserved_regions (list): List of tuples representing the start and end positions of conserved regions 
    """
    # Compute the minimum length of all genomes
    min_length = min(len(genome) for genome in genomes)
    
    # Iterate over each position in the first genome
    conserved_regions = []
    for i in range(min_length):
        # Check if the nucleotides at this position are the same in all genomes
        if all(genome[i] == genomes[0][i] for genome in genomes):
            # If they are, extend the current conserved region
            if not conserved_regions or i != conserved_regions[-1][1] + 1:
                conserved_regions.append((i, i))
            else:
                conserved_regions[-1] = (conserved_regions[-1][0], i)
    
    return conserved_regions
