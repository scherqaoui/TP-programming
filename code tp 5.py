# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 06:37:25 2023

@author: janna
"""

import numpy as np, itertools, time 

#task 1

DNA_sample = ['ACCATACCTTCGATTGTCGTGGCCACCCTCGGATTACACGGCAGAGGTGC',
               'GTTGTGTTCCGATAGGCCAGCATATTATCCTAAGGCGTTACCCCAATCGA',
               'TTTTCCGTCGGATTTGCTATAGCCCCTGAACGCTACATGCACGAAACCAC',
               'AGTTATGTATGCACGTCATCAATAGGACATAGCCTTGTAGTTAACAG',
               'TGTAGCCCGGCCGTACAGTAGAGCCTTCACCGGCATTCTGTTTG',
               'ATTAAGTTATTTCTATTACAGCAAAACGATCATATGCAGATCCGCAGTGCGCT',
               'GGTAGAGACACGTCCACCTAAAAAAGTGA',
               'ATGATTATCATGAGTGCCCGGCTGCTCTGTAATAGGGACCCGTTATGGTCGTGTTCGATCAGAGCGCTCTA',
               'TACGAGCAGTCGTATGCTTTCTCGAATTCCGTGCGGTTAAGCGTGACAGA',
               'TCCCAGTGCACAAAACGTGATGGCAGTCCATGCGATCATACGCAAT',
               ' GGTCTCCAGACACCGGCGCACCAGTTTTCACGCCGAAAGCATC', 
               'AGAAGGATAACGAGGAGCACAAATGAGAGTGTTTGAACTGGACCTGTAGTTTCTCTG',
               'ACGAAGAAACCCACCTTGAGCTGTTGCGTTGTTGCGCTGCCTAGATGCAGTGG',
               'TAACTGCGCCAAAACGTCTTCCAATCCCCTTATCCAATTTAACTCACCGC',
               'AATTCTTACAATTTAGACCCTAATATCACATCATTAGACACTAATTGCCT', 
               'TCTGCCAAAATTCTGTCCACAAGCGTTTTAGTTCGCCCCAGTAAAGTTGT',
               'TCAATAACGACCACCAAATCCGCATGTTACGGGACTTCTTATTAATTCTA',
               'TTTTTCGTGGGGAGCAGCGGATCTTAATGGATGGCGCCAGGTGGTATGGA']


def hamming_distance(s1,s2):
    count = 0
    for i in range (len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

print(hamming_distance(DNA_sample[0],DNA_sample[1]))


#task 2
def levenshtein_distance(s1,s2):
    m=len(s1)
    n=len(s2)
    table = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(m+1):
        table[i][0]=i
    for j in range (n+1):
        table[0][j]=j
        
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1+min(table[i-1][j], table[i][j-1], table[i-1][j-1])
    return table[-1][-1]
            
print(levenshtein_distance("risk","think"))    
print(levenshtein_distance("python","krythonite"))
print(levenshtein_distance(DNA_sample[0],DNA_sample[1]))


storing_results = []
for x in DNA_sample:
    leven_dist = []
    for y in DNA_sample:
        leven_dist.append(levenshtein_distance(x,y))
    storing_results.append(leven_dist)
print(storing_results)  

#task 3



def smith_waterman(sequence1, sequence2, match_score=3, gap_cost=2):
    sequence1, sequence2 = sequence1.upper(), sequence2.upper()
    # Construct the scoring matrix
    scoring_matrix = np.zeros((len(sequence1) + 1, len(sequence2) + 1))
    for i, j in itertools.product(range(1, scoring_matrix.shape[0]), range(1, scoring_matrix.shape[1])):
        match = scoring_matrix[i - 1, j - 1] + (match_score if sequence1[i - 1] == sequence2[j - 1] else -match_score)
        delete = scoring_matrix[i - 1, j] - gap_cost
        insert = scoring_matrix[i, j - 1] - gap_cost
        scoring_matrix[i, j] = max(match, delete, insert, 0)
    #  find the optimal alignment
    aligned_sequence, end_position = traceback(scoring_matrix, sequence2)
    return end_position, end_position + len(aligned_sequence)

def traceback(scoring_matrix, sequence, aligned_sequence='', old_i=0):
    flipped_matrix = np.flip(np.flip(scoring_matrix, 0), 1)
    i_, j_ = np.unravel_index(flipped_matrix.argmax(), flipped_matrix.shape)
    i, j = np.subtract(scoring_matrix.shape, (i_ + 1, j_ + 1))
    if scoring_matrix[i, j] == 0:
        return aligned_sequence, j
    
    separator = '-' if old_i - i > 1 else ''
    # Build the aligned sequence
    aligned_sequence = sequence[j - 1] + separator + aligned_sequence
    return traceback(scoring_matrix[0:i, 0:j], sequence, aligned_sequence, i)




print('smith-water:',smith_waterman(DNA_sample[0], DNA_sample[1]))
   






























































