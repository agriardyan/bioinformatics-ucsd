def approximate_pattern_matching(pattern, genome, tolerance):
	resultArr = []
	k = len(pattern)
	genomeLen = len(genome)
	for i in range(genomeLen - k + 1):
		comparedKmer = genome[i : i+k]
		if(hamming_distance(pattern, comparedKmer) <= tolerance):
			resultArr.append(i)
	return resultArr

def hamming_distance(kmer1, kmer2):
    counter = 0
    kmer1Len = len(kmer1)
    for i in range(kmer1Len):
        if(kmer1[i] != kmer2[i]):
            counter += 1
    return counter