"""
https://stepik.org/lesson/5164/step/1

CS: Solving the Median String Problem
"""
import sys

def calc_hamming_dist(p1, p2):
    d = 0
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            d += 1
    return d

def distance_between_pattern_and_strings(pattern, dnas):
    k = len(pattern)
    distance = 0
    for dna in dnas:
        hamming_dist = sys.maxsize
        for i in range(0, len(dna)-k+1):
            kmer_pattern = dna[i:i+k]
            hamming_dist_result = calc_hamming_dist(pattern, kmer_pattern)
            if hamming_dist > hamming_dist_result:
                hamming_dist = hamming_dist_result
        distance += hamming_dist
    return distance

if __name__ == "__main__":
    dna_sequences = ""
    pattern = ""

    with open("bio1/week3/dataset_5164_1.txt", "r") as inp:
        input_items = inp.read().strip().splitlines()
        pattern = input_items[0].strip()
        dna_sequences = input_items[1].strip().split()
    
    dist = distance_between_pattern_and_strings(pattern, dna_sequences)
    print(dist)
