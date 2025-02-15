import math

def score(matrix):
    # Initialize a dictionary to store the counts
    column_counts = [{'A': 0, 'T': 0, 'G': 0, 'C': 0} for _ in range(len(matrix[0]))]

    # Iterate over each column index
    for col in range(len(matrix[0])):
        # Iterate over each row
        for row in matrix:
            nucleotide = row[col]
            column_counts[col][nucleotide] += 1

    # Print the counts for each column
    for i, counts in enumerate(column_counts):
        print(f"Column {i+1}: {counts}")
    
    # calculate percentage of each nucleotide in each column
    for i, counts in enumerate(column_counts):
        total = sum(counts.values())
        for key in counts:
            column_counts[i][key] = counts[key] / total
        
    # Print the percentage for each column
    for i, counts in enumerate(column_counts):
        print(f"Column {i+1}: {counts}")
    
    # calculate the consensus string
    consensus = ''
    for counts in column_counts:
        max_nucleotide = max(counts, key=counts.get)
        consensus += max_nucleotide

    print(f"Consensus: {consensus}")

    # calculate the entropies for each column
    entropies = []
    for counts in column_counts:
        entropy = 0
        for key in counts:
            prob = counts[key]
            if prob == 0:
                continue
            entropy += prob * math.log2(prob)
        entropies.append(-entropy)

    # Print the entropies for each column
    for i, entropy in enumerate(entropies):
        print(f"Column {i+1}: {entropy}")

    # calculate the score
    score = sum(entropies)
    print(f"Score: {score}")

matrix = [
    'TCGGGGGTTTTT',
    'CCGGTGACTTAC',
    'ACGGGGATTTTC',
    'TTGGGGACTTTT',
    'AAGGGGACTTCC',
    'TTGGGGACTTCC',
    'TCGGGGATTCAT',
    'TCGGGGATTCCT',
    'TAGGGGAACTAC',
    'TCGGGTATAACC'
]
score(matrix)