import math
import sys
import numpy as np

from week3_motif_enumeration import _mutate

def entropy(arr):
    result = 0
    for x in arr:
        result += x*math.log2(x)
    return -result

def hamming(p1, p2):
    d = 0
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            d += 1
    return d

def process(dna_1D,k):
    dna_2D = list()
    entropies = list()
    for dna in dna_1D:
        dna_2D.append(list(dna))
    arr = np.array(dna_2D)
    
    row_len, column_len = arr.shape
    consensus_nucleotides = list()
    
    for i in range(column_len):
        nucleotides, counts = np.unique(arr[:,i], return_counts=True)
        print('Uq', np.unique(arr[:,i], return_counts=True))
        print('Argmax', np.argmax(counts))
        consensus = nucleotides[np.argmax(counts)]
        consensus_nucleotides.append(consensus)
        entropies.append(entropy(counts/row_len))
    
    assert len(entropies) == column_len
    
    minim = 1000
    minim_idx = -1
    for i,_ in enumerate(entropies):
        if i+k > column_len:
            break

        val = np.sum(entropies[i:i+k])
        print('minim',minim)
        print('val',val)
        if(minim < val):
            minim = val
            minim_idx = i
    
    return nucleotides, minim_idx

def median_string(dnas, k):
    initial_dna = list(dnas[0])
    dna_len = len(initial_dna)
    kmers = set()
    for i,_ in enumerate(initial_dna):
        if(i+k > dna_len):
            break
        
        kmer = dnas[0][i:i+k]
        kmers.add(kmer)

    print('kmers', kmers)
    
    min = sys.maxsize
    median = ''
    median_map = dict()
    for i, kmer in enumerate(kmers):
        count = 0
        for dna in dnas[1:]:
            dna_arr = list(dna)
            localmin = sys.maxsize
            for idna, _ in enumerate(dna_arr):
                if(idna+k > dna_len):
                    break

                comparedKmer = dna[idna:idna+k]
                val = hamming(kmer, comparedKmer)
                if(val < localmin):
                    localmin = val
            count += localmin
        median_map[kmer] = count
    
    for key_m, val_m in median_map.items():
        if(val_m < min):
            median = key_m
        
    return median
        
    
            



if __name__ == "__main__":
    dna_1D = [
        "GCTCTCCACAGAAAGTGTTATACGCTTGGAGAGACGGTGGTA",
        "GCGCACAAGTGTGGCGGGTGTTTAATTCTAGGCGGTCTACCA",
        "GGCGAAGAACAAAAGGCGATTCATCAGAGGGAGTGTGTCACG",
        "CGCGGGGCAACCTATTTAGGATGGAAATTACAGTGTGCGATA",
        "AGGAGATCGAGCAAGTGTGATTGGTGAGATCCAAACAGAGCA",
        "CCTGCCGATCAAGATGCAGTCAAAAGGACGGTATGAAAGTGT",
        "TCCAAACGTTACTAGTGTTGCTATAGTTAGTAACAGTCGTAG",
        "TGAGACTAGTGTACCGTATCGGGCGCAACACACGGAAGGCTA",
        "GCTTATATGGACCTGGACACCCTATGAGTAAAGTGTTAACCC",
        "CCTCGTCAGTGTACTTGTATGTCATATGTCGACTTAATGCAA"
    ]
    minKmer = median_string(dna_1D, 6)
    print(minKmer)
    pass