def extract_conserved_regions(aln):
    conserved_regions = []
    num_seqs = len(aln)
    aln_length = aln.get_alignment_length()

    for i in range(aln_length):
        column = aln[:, i]
        if len(set(column)) == 1:
            conserved_regions.append((i, i))
        elif len(set(column)) < num_seqs:
            groups = []
            for seq in aln:
                group_id = None
                for j, group in enumerate(groups):
                    if column[seq.id] in group:
                        group_id = j
                        break
                if group_id is None:
                    groups.append(set([column[seq.id]]))
                else:
                    groups[group_id].add(column[seq.id])
            groups = sorted(groups, key=len, reverse=True)
            consensus = groups[0]
            for group in groups[1:]:
                if consensus.intersection(group):
                    consensus = consensus.intersection(group)
                else:
                    break
            if len(consensus) > 1:
                start = i
                while i < aln_length - 1 and len(set(aln[:, i+1])) < num_seqs and set(aln[:, i+1]).issubset(consensus):
                    i += 1
                conserved_regions.append((start, i))

    return conserved_regions
