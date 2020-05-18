import sys

def structure_matrix(raw_matrix_str):
    assert len(raw_matrix_str) == 4

    col_len = len(raw_matrix_str[0].split())
    matrix = [dict() for _ in range(col_len)]

    for i,row in enumerate(raw_matrix_str):
        cells = row.split()
        for j,c in enumerate(cells):
            x = float(c)
            if i == 0:
                matrix[j]['A'] = x
            elif i == 1:
                matrix[j]['C'] = x
            elif i == 2:
                matrix[j]['G'] = x
            else:
                matrix[j]['T'] = x

    assert len(matrix) == col_len

    return matrix

def calculate_profile_most_probable(dna, k, prob_matrix):
    max_prob = 0
    max_idx = -1
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i+k]
        sum_prob = 1
        for j,s in enumerate(kmer):
            sum_prob *= prob_matrix[j][s]
        if sum_prob > max_prob:
            max_prob = sum_prob
            max_idx = i

    assert max_idx > -1
    return dna[max_idx:max_idx+k]


if __name__ == '__main__':
    filename = "profile_most_probable_dataset.txt"
    content = list()
    dna = ''
    k = 0
    raw_matrix_str = list()
    with open(filename, 'r') as file:
        raw_content = file.read().rstrip()
        content = raw_content.split('\n')

    assert len(content) > 3

    dna = content[0]
    k = int(content[1])
    raw_matrix_str = content[2:]

    matrix = structure_matrix(raw_matrix_str)
    result = calculate_profile_most_probable(dna, k, matrix)
    print(result)