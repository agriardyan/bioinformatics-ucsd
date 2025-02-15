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

def immediate_neighbors(pattern):
	"""
	https://stepik.org/lesson/3014/step/1?unit=8228
	"""
	nucleotides = ['A', 'T', 'G', 'C']
	neighborhoods = set()
	for i,v in enumerate(pattern):
		for _,n in enumerate(nucleotides):
			if(n == v):
				continue

			neighbor = pattern[:i] + n + pattern[i+1:]
			neighborhoods.add(neighbor)
	
	return neighborhoods

def neighbors(pattern, d):
	"""
	https://stepik.org/lesson/3014/step/3?unit=8228
	"""

	if d == 0:
		return set(pattern)
	
	nucleotides = {'A', 'T', 'G', 'C'}
	if len(pattern) == 1:
		return nucleotides	
	
	neighborhood = set()
	suffix_neighbors = neighbors(pattern[1:], d)

	for i,val in enumerate(suffix_neighbors):
		if hamming_distance(pattern[1:], val) < d:
			for _,n in enumerate(nucleotides):
				neighborhood.add(n + val)
			else:
				neighborhood.add(pattern[0] + val)
	
	return neighborhood

results = neighbors('CGAGACTTACTC', 3)
for k,v in enumerate(results):
	with open("test.txt", "a") as myfile:
		myfile.write(v + ' ')
	