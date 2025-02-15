# In bioinformatics, the median string is an algorithm used to find a consensus sequence (or motif) from a set of DNA sequences. 
# The goal is to identify a string that represents the most common elements across all sequences in the set.

# How It Works
# Input: A set of DNA sequences.
# Process: The algorithm generates all possible substrings (l-mers) of a specified length from each sequence.
# Consensus: It then finds the substring that appears most frequently across all sequences. This substring is the median string or consensus sequence.

# Applications
# Gene Regulatory Motifs: Identifying regulatory motifs that control gene expression.
# Pattern Recognition: Finding common patterns in DNA sequences.

# The median string algorithm is computationally intensive, especially for longer substrings, but it's a fundamental tool in bioinformatics for motif discovery.


import sys
import itertools

def _hamming_distance(a, b):
    assert len(a) == len(b)
    d = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            d += 1
    return d

def median_string(consensus_kmer_dict, dnas, k):
    assert len(dnas) > 1

    for i, _ in enumerate(dnas):
        kmer_set = _convert_to_kmer_set(dnas[i], k)
        for compared_kmer in kmer_set:
            if compared_kmer in consensus_kmer_dict:
                consensus_kmer_dict[compared_kmer] += 1
                continue
            else:
                nearest_origin_kmer, nearest_hamming_dist = _find_minimal_hamming_distance(compared_kmer, consensus_kmer_dict)
                consensus_kmer_dict[nearest_origin_kmer] += 1

    median_string = ""
    max_point = 0
    for med_kmer, point in consensus_kmer_dict.items():
        if point > max_point:
            max_point = point
            median_string = med_kmer

    return median_string


def _find_minimal_hamming_distance(compared_kmer, origin_kmer_dict):
    minimal_hamming_dist = sys.maxsize
    minimal_hamming_kmer = ''
    for origin_kmer, origin_hamming_dist in origin_kmer_dict.items():
        result = _hamming_distance(compared_kmer, origin_kmer)
        if result < minimal_hamming_dist:
            minimal_hamming_dist = result
            minimal_hamming_kmer = origin_kmer
    return minimal_hamming_kmer, minimal_hamming_dist


def _convert_to_kmer_set(dna, k):
    kmer_set = set()
    dna_arr = list(dna)
    for i in range(len(dna_arr) - k + 1):
        kmer = dna_arr[i:i + k]
        kmer_str = ''.join(kmer)
        kmer_set.add(kmer_str)
    return kmer_set


if __name__ == '__main__':

    base = ['A', 'T', 'G', 'C']

    filename = "median_string_dataset.txt"
    content = list()
    k = 0
    dnas = list()
    with open(filename, 'r') as file:
        raw_content = file.read().rstrip()
        content = raw_content.split('\n')

    assert len(content) > 2

    k = int(content[0])
    dnas = content[1:]

    perms = itertools.product(base, repeat=k)
    ground_truth_set = set()
    ground_truth_dict = dict()
    for p in perms:
        origin_kmer = ''.join(p)
        ground_truth_set.add(origin_kmer)
        ground_truth_dict[origin_kmer] = 1

    result = median_string(ground_truth_dict, dnas, k)
    print(result)

