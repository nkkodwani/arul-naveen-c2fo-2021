''' STICK BREAKNG PROBLEM: Pseudocode:
Input:
    l = length of stick to cut; l < 1000
    n = number of cuts to be made; n < 50
    c1, c2, c3.... , cn = where cuts will be done
        must be in increasing order

    determining cut cost: 
    cut_cost = l
    l = l - cut
'''
import numpy as np

def stick_break(l, n: int, cuts: list):
    if l > 999 or l < 2:
        return "Invalid stick length"
    if n > 49:
        return "Invalid number of cuts"
    a1 = np.empty((len(cuts), len(cuts)))
    
    #cut_cost = l
    # l = l - cut
    
    return cuts[n-1], a1
    


cuts = []
l = int(input("Length of stick to be cut: "))
n = int(input("Number of cuts to be made: "))
print("Input cuts in increasing order: ")
for i in range (n):
    c = int(input("\tInput cut position: "))
    if c > l: 
        print("Input valid position")
    cuts.append(c)
print(stick_break(l, n, cuts))

