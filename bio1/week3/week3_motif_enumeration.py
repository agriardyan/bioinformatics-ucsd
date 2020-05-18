def motif_enumeration(dnaList, k, d):
    kmer_list = [set() for _ in dnaList]
    for pos, pattern in enumerate(dnaList):
        patternLen = len(pattern)
        allMutationSet = set()
        for k_pos in range(patternLen - k + 1):
            mutationSet = _mutate(pattern[k_pos:k_pos+k], d)
            allMutationSet = allMutationSet.union(mutationSet)
        kmer_list[pos] = allMutationSet

    finalMutationSet = kmer_list[0]
    for m in kmer_list:
        finalMutationSet = finalMutationSet&m

    return finalMutationSet

base = {'A', 'T', 'G', 'C'}

def _mutate(kmer, d):

    mutationSetList = []

    mutationSet = _mutateOnce(kmer)
    if d > 1:
        return mutationSet

    mutationSetList.append(mutationSet)

    for _ in range(d-1):
        for mutation in mutationSet:
            newMutationSet = _mutateOnce(mutation)
            mutationSetList.append(newMutationSet)
    
    for m in mutationSetList:
        mutationSet = mutationSet.union(m)
    
    return mutationSet

def _mutateOnce(kmer):
    mutationSet = set()
    for i,s in enumerate(kmer):
        for b in base:
            mutation = kmer[:i] + b + kmer[i+1:]
            
            mutationSet.add(mutation)
    return mutationSet

if __name__ == "__main__":
    print('Hello')
    dnaList = [
    "TCACGCACAGGATGCGCGTGGATAC",
    "TAATCTGAGCAGTCAGTTGGGATAC",
    "AGTGTGATTCGAAACAAAAAATGAT",
    "TCCTAATACGAATTTGACACCGGTG",
    "ATGTTGAAACAATTGCCGAGAAGTC",
    "GTCTTTCCAGGCTGGGAAACGCTCG"
    ]
    k = 5
    d = 1
    result = motif_enumeration(dnaList, k, d)
    print(sorted(result))
    pass