"""
https://stepik.org/lesson/204/step/7?unit=8251
Generate the (3,2)-mer composition
"""

def find_pair(read, k, d):
    read_ln = len(read)
    limit = read_ln - k - k - d + 1
    pairs = []
    print(limit)
    for i in range(limit):
        front_read = read[i:i+k]
        back_read = read[i+k+d:i+k+d+k]
        pairs.append("(" + front_read + "|" + back_read + ")")
    
    pairs.sort()
    return pairs
    

pairs = find_pair('TAATGCCATGGGATGTT', 3, 2)
print(" ".join(pairs))