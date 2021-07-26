# Recursion and dynamic programming: 7/23 puzzle - the 'Edit Distance' problem
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
#    Insert a character
#    Delete a character
#    Replace a character
# #I could not figure out the edit distance problem, so I used dynamic programming to do the fibbonaci sequence

import numpy as np #this will be for arrays

#fibonnaci recursively:
def fibb(n):
    if n <= 2:
        return 1
    else: 
        return fibb(n-1) + fibb(n-2) #to make this dynamic programming, save repeated results in an array

n = int(input("Input a number: "))
print("Recursive:")
print(f"\t{fibb(n)}")


#fibonnaci using dynamic programming:
def fibbDP(n):
    a = 2
    fibb = np.empty(n + 1)
    fibb[0] = 0
    fibb[1] = 1
    while a <= n:
        fibb[a] = fibb[a-1] + fibb[a-2]
        a += 1
    return fibb[n]


