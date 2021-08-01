''' STICK BREAKNG PROBLEM: Pseudocode:
Input:
    l = length of stick to cut; l < 1000
    n = number of cuts to be made; n < 50
    c1, c2, c3.... , cn = where cuts will be done
        must be in increasing order

Method(startIndex, endIndex):
    define where cuts should be made
    create 2d array of integers l columns l rows
    memoize result in array arr[start][end]
        if result for specific cut already exists: return that result
    length = end - start
    subcutcost = infinity
    for i in range (indexstart, indexend):
        if i in [cuts]
            cost = length + cutMethod(start, i) + cutMethod(i, end)
            replace subcutcost if cost < subcutcost

    return subcutcost
    
'''
import numpy as np
# import sys
# sys.setrecursionlimit(1001)

#INPUT: Cuts and length
cuts = []
l = int(input("Length of stick to be cut: "))
if l > 999 or l < 2:
    print("Invalid stick length")
n = int(input("Number of cuts to be made: "))
if n > 49:
    print("Invalid number of cuts")
print("Input cuts in increasing order: ")
for i in range (n):
    c = int(input("\tInput cut position: "))
    if c > l: 
        print("Input valid position")
    cuts.append(c)

#INITIALIZE ARRAY
a1 = np.array((l+1,l+1))            # is itpossible to make the values infinity instead of empty?
                                    # the array is 2d. The first index will be start (vertical) and second index will be end (horizontal)
                                    # this allows for all combinations of start/end indexes to be tested 
                                    # What value should I put in this array?
    
# for i in range(l+1):
#     for j in range(l+1):
#         a1[i][j] = 1

#METHOD
def cutCost(start: int, end: int): #start index; cuts list; stick size 
    memoizedResult = a1[start][end]
    if memoizedResult: #fails if value is empty
        return memoizedResult

    length = end - start

    minCutCost = float('inf')

    for i in range (start, end):
        if i in cuts:
            cost = length + cutCost(start, i) + cutCost(i, end) #reached max recursion depth here
            if cost < minCutCost:
                minCutCost = cost

    if minCutCost == float('inf'):
        minCutCost = 0

    a1[start][end] = minCutCost

    return minCutCost

#INPUT

print(cutCost(0, l))



