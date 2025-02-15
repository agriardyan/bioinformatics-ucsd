import random

# RandomizedMotifSearch(Dna, k, t)
#     randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
#     BestMotifs ← Motifs
#     while forever
#         Profile ← Profile(Motifs)
#         Motifs ← Motifs(Profile, Dna)
#         if Score(Motifs) < Score(BestMotifs)
#             BestMotifs ← Motifs
#         else
#             return BestMotifs

def randomized_motif_search(dna, k, t):
    motifs = []
    for sequence in dna:
        start = random.randint(0, len(sequence) - k)
        motifs.append(sequence[start:start + k])

    best_motifs = motifs

    while True:
        profile = profile_motifs(motifs)
        motifs = motifs_from_profile(profile, dna)
        if score_motifs(motifs) < score_motifs(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs
    
def profile_motifs(motifs):
    profile = []
    for i in range(len(motifs[0])):
        column = [motif[i] for motif in motifs]
        profile.append([column.count(base) / len(column) for base in 'ACGT'])
    return profile

def motifs_from_profile(profile, dna):
    k = len(profile)
    motifs = []
    for sequence in dna:
        best_prob = 0
        best_motif = ''
        for i in range(len(sequence) - k + 1):
            kmer = sequence[i:i + k]
            prob = 1
            for j, base in enumerate(kmer):
                prob *= profile[j]['ACGT'.index(base)]
            if prob > best_prob:
                best_prob = prob
                best_motif = kmer
        motifs.append(best_motif)
    return motifs

def score_motifs(motifs):
    score = 0
    for i in range(len(motifs[0])):
        column = [motif[i] for motif in motifs]
        score += len(column) - max([column.count(base) for base in 'ACGT'])
    return score

# Test the implementation
def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Extract k and t from the first line
        k, t = map(int, lines[0].strip().split())
        
        # Extract DNA sequences from the second line
        dna_sequences = lines[1].strip().split()
        
        return k, t, dna_sequences

file_path = 'bio1/week4/randomized_motif_search.txt'
k, t, dna = parse_file(file_path)

motifs = randomized_motif_search(dna, k, t)
for motif in motifs:
    print(motif)