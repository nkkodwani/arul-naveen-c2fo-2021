'''
LEETCODE PROBLEM 1092:
    Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  
    If multiple answers exist, you may return any of them.  
    (A string S is a subsequence of string T if deleting some number of characters from T 
    (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

    EXAMPLE: T = 'abac' ; S = 'cab' 
        Output = 'cabac' - contains T and S
    
    1 <= len(str1), len(str2) <= 1000
    str1 and str2 consist of lowercase English letters

    Hint: We can find the length of the longest common subsequence between str1[i:] and str2[j:] (for all (i, j)) 
     by using dynamic programming. We can use this information to recover the longest common supersequence.

INPUT: 
    T: the larger string
    S: a subset of T made of characters in T 

OUTPUT: 
    strOut: shortest string that has S and  T as subsequences

'''

import numpy as np

#Input:
str1 = str(input("Please input T: "))
str2 = str(input("Please input S (subsequence of T): "))

#Create array: 
arr = np.zeros(())

def commonSubsequence(str1: str, str2: str):
    #Make sure input is valid length - check 1 < inp < 1000 and len(str2) < len(str1) 
    if (len(str1) <= 1) or (len(str2) <= 1) or (len(str1) >= 1000) or (len(str2) >= 1000) or (len(str2) > len(str1)):
        return "Invalid input."
    #Make sure str2 is a subsequence of str1
    valid = True
    for i in range(len(str2)):
        if str2[i] not in str1: #What if str2[i] is a repeat character? Ex: str1 = 'Naveen', str2 = 'eeee'; valid would still be True
            valid = False
            break
    if not valid:
        return "Invalid strings. "
    #simple scenarios:
    if str2 in str1:
        return str1
    

    #Now fill array: 
    

#Call method: 
print(commonSubsequence(str1, str2))

