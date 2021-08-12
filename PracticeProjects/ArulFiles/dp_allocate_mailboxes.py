'''
LEETCODE PROBLEM 1478: 
    Given the array houses and an integer k. where houses[i] is the location of the ith house along a street, your task is to allocate k mailboxes in the street.
    Return the minimum total distance between each house and its nearest mailbox.
    https://leetcode.com/problems/allocate-mailboxes/

INPUT:
    hosues = list of house position in increasing order
    int n_mailbox = number of mailboxes (k in Leetcode problem)

OUTPUT: 
    minimum total distance between houses and mailbox
    ex: 3 houses at [1, 5, 20] and 2 mailboxes:
        ouput = 4
        mailboxes placed at 3 and 20; minimum output = 4 = (3-1) + (5-3) + (20-20) 

PSEUDOCODE: 
    create array with length of the largest house position + 1
    split array down the diagonal - this prevents computations from being repeated
    for mb1_pos in range(1, houses[-1]+1): 
        for mb2_pos in range(mb1_pos, houses[-1]+1): 
            minDistHouse = []
            record total distance of mailbox from houses in a1 array (see formula at end of pseudocode - this will fill array)
            for house_pos in houses_pos:
                if abs(house_pos - mb1_pos) < abs(house_pos - mb2_pos) 
                    minDistHouse.append(abs(house_pos - mb1_pos))
                else: 
                    minDistHouse.append(abs(house_pos - mb2_pos))

    when array is filled, return minimum distance (seach array for minimum distance)

    array[mb1_pos][mb2_pos] = abs(house[0] - mailbox[0]) + abs(house[1] + mailbox[1]) + abs(house[2] + mailbox[2]) ... 

'''

import numpy as np
import statistics as st


#INPUT: 
num_houses = int(input("Input the number of houses: "))
houses_pos = []
for i in range (num_houses):
    house = int(input("Input house position: "))
    houses_pos.append(house)
# k = int(input("Input the number of mailboxes: "))
k = 2 #for now while testing the minimum position

#SETUP:
a1 = np.zeros((houses_pos[-1] + 1, houses_pos[-1] + 1))
a1.fill(100000)
    # vertical axis will be mailbox 1, 
    # horizontal axis will be mailbox 2, ...


def allocate_mailboxes(houses_pos:list, k:int):
    #Make sure input falls into constraints
    n = len(houses_pos)

    if n >= 100 or n <= 1:
        print("Error: Invalid number of houses.")
        return -1
    if houses_pos[-1] > 10000:
        print("Too large of house position. Restart and try < 10000")
        return -1
    if k > n or k < 1:
        print("Invalid number of mailboxes.")
        return -1

    #Some cases where solving is simple:
    if k == n:
        mailboxes = houses_pos
        return 0
    
    if n == 2:
        return (abs(houses_pos[0] - houses_pos[1]))
    
    if k == 1: #From hint1 on leetcode page - return median of list if k=1
        return (st.median(houses_pos))

    #solution
    for mb1_pos in range(1, houses_pos[-1]+1): 
        for mb2_pos in range(mb1_pos, houses_pos[-1]+1): 
            minDistHouse = []
            #record total distance of mailbox from houses in a1 array (see formula at end of pseudocode - this will fill array)
            for house_pos in houses_pos:
                if abs(house_pos - mb1_pos) < abs(house_pos - mb2_pos): #if the house is closer to mb1, then use mb1
                    minDistHouse.append(abs(house_pos - mb1_pos))
                else: 
                    minDistHouse.append(abs(house_pos - mb2_pos))
            a1[mb1_pos][mb2_pos] = sum(minDistHouse) 
    
    return np.amin(a1)


print(allocate_mailboxes(houses_pos, k))

'''

'''
    