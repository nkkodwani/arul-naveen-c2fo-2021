''' STICK BREAKNG PROBLEM: Pseudocode:
Input:
    l = length of stick to cut; l < 1000
    n = number of cuts to be made; n < 50
    c1, c2, c3.... , cn = where cuts will be done
        must be in increasing order

Method(startIndex, endIndex):
    create 2d array of integers l+1 columns l+1 rows
    check if arr[start][end] has already been calculated
        if result for specific cut already exists: return that result
    subcutcost = infinity 
    for i in range (start, end):
        if i in [cuts]
            cost = length + cutMethod(start, i) + cutMethod(i, end)
            replace subcutcost if cost < subcutcost
    store subcutcost in arr[start][end] - only stores if the value is empty
    return subcutcost
    
'''
import numpy as np

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
a1 = np.zeros((l+1,l+1))            # fills array, value will be overwritten by memozied result
                                    # the array is 2d. The first index will be start (vertical) and second index will be end (horizontal)
                                    # this allows for all combinations of start/end indexes to be tested

#METHOD
def cutCost(start: int, end: int): #start index; cuts list; stick size 

    memoizedResult = a1[start][end] #if the calcuation for a specific cut has already been done, then return that result
    if memoizedResult != 0: 
        return memoizedResult

    length = end - start #need to store length of piece being cut as it is factored into the cost

    minCutCost = float('inf') 

    for i in range (start+1, end): #needs to start at start+1 because if start is included, line 56 will have infinite recursion
        if i in cuts:
            cost = length + cutCost(start, i) + cutCost(i, end)     # the cost is equal to the length of the stick + the cost of the cuts. 
                                                                    # this line uses recursion to calculate the cost of each cut 
                                                                    # each time recusrion is used, it adds one more cut
                                                                    # therefore it recurses one time for each cut inputted
            if cost < minCutCost:  #replace mincutcost with new minimum cost
                minCutCost = cost

    if minCutCost == float('inf'): #if none of the values in range(start, end) are in cuts list, make mincutcost != 'inf'
        minCutCost = 0

    a1[start][end] = minCutCost #save the minimum cut cost in the array
    
    return minCutCost

#Now just test method
print(cutCost(0, l))



