import sys
import numpy as np

def _convert_to_kmer_char_list(dna, k):
    kmer_list = list()
    dna_arr = list(dna)
    for i in range(len(dna_arr) - k + 1):
        kmer = dna_arr[i:i + k]
        kmer_list.append(kmer)
    return kmer_list

def _build_initial_best_motif(dna_list, k):
    dna_list_len = len(dna_list)
    motif = list()
    for i,dna in enumerate(dna_list):
        motif.append(list(dna[:k]))
    return motif

def _build_motif_matrix(dna_list, k):
    matrix = np.zeros((4,k))
    dnas_np_arr = np.array(dna_list)
    for i in range(k):
        search_res_list = _convert_dna_col_to_probability(dnas_np_arr[:,i])
        matrix[:,i] = search_res_list
    return matrix

def _score_motif_matrix(motif_list, motif_matrix):
    motif_np_list = np.array(motif_list)
    shape = motif_np_list.shape
    assert len(shape) == 2
    original_matrix = motif_matrix * shape[0]
    score = np.sum(original_matrix, axis=0) - np.max(original_matrix, axis=0)
    return np.sum(score)

base = ('A', 'C', 'G', 'T')
def _convert_dna_col_to_probability(dna_col_np_arr):
    search_res_list = list()
    shape = dna_col_np_arr.shape
    assert len(shape) == 1
    for b in base:
        search_res = np.where(dna_col_np_arr == b)
        assert len(search_res) > 0
        proba = len(search_res[0])/shape[0]+1 # THE WHOLE ENHANCEMENT IS A SMALL ADITION OF +1 HERE HAHA :D
        search_res_list.append(proba)
    assert len(search_res_list) == len(base)
    return search_res_list


def calculate_next_motif(raw_dna_list, k):
    assert len(raw_dna_list) > 0
    first_dna_list = _convert_to_kmer_char_list(raw_dna_list[0], k)
    assert len(first_dna_list) == len(raw_dna_list[0]) - k + 1

    best_motif = _build_initial_best_motif(raw_dna_list, k)
    best_motif_matrix = _build_motif_matrix(best_motif, k)
    best_motif_score = _score_motif_matrix(best_motif, best_motif_matrix)

    for i,kmer in enumerate(first_dna_list):
        current_motif = list()
        current_motif.append(kmer)
        current_motif_matrix = _build_motif_matrix(current_motif, k)
        for j,raw_dna in enumerate(raw_dna_list[1:]):
            max = -sys.maxsize - 1
            profile_most_probable = []
            next_kmer_list = _convert_to_kmer_char_list(raw_dna, k)
            for next_kmer in next_kmer_list:
                next_kmer_np = np.reshape(next_kmer, newshape=(-1,k))
                next_kmer_matrix = _build_motif_matrix(next_kmer_np, k)
                multiply_result = np.multiply(current_motif_matrix, next_kmer_matrix)
                prod_result = np.prod(np.sum(multiply_result, axis=0))
                if prod_result > max:
                    max = prod_result
                    profile_most_probable = next_kmer

            # add the profile_most_probable into current_motif and recalculate the current_motif_matrix
            current_motif.append(profile_most_probable)
            current_motif_matrix = _build_motif_matrix(current_motif, k)
        assert len(current_motif) == len(raw_dna_list)
        current_motif_score = _score_motif_matrix(current_motif, current_motif_matrix)
        if current_motif_score < best_motif_score:
            best_motif = current_motif
            best_motif_matrix = current_motif_matrix
            best_motif_score = current_motif_score

    return best_motif, best_motif_matrix, best_motif_score

if __name__ == '__main__':

    filename = "greedy_motif_enhanced_dataset.txt"
    content = list()
    dna = ''
    k = 0
    t = 0
    raw_matrix_str = list()
    with open(filename, 'r') as file:
        raw_content = file.read().rstrip()
        content = raw_content.split('\n')

    raw_k_t = content[0]
    k_t = raw_k_t.split()
    assert len(k_t) == 2
    k = int(k_t[0])
    t = int(k_t[1])
    raw_dna_list = content[1:]

    best_motif, best_motif_matrix, best_motif_score = calculate_next_motif(raw_dna_list, k)
    for motif in best_motif:
        print(''.join(motif))
