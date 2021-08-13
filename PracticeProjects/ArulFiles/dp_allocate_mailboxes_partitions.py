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
    Base Cases: 
        k = 1 : put mailbox in median (given by leetcode hint)
        k = # of houses : put one mailbox at each house (total distance is 0)

    partition: 
    break houses into k groups --> this makes it so each group has one mailbox (base case)
        from leetcode discussion: form one group, then form k-1 groups with remaining elements (recursion)




'''

import numpy as np
import statistics as st


#INPUT: 
num_houses = int(input("Input the number of houses: "))
houses_pos = []
for i in range (num_houses):
    house = int(input("Input house position: "))
    houses_pos.append(house)
k = int(input("Input the number of mailboxes: ")) 

#CREATE MEMO TABLE: 
a1 = np.zeros(shape=(houses_pos[-1], houses_pos[-1]))
a1.fill(-1)
#right now this is not being used


#start index will be first house pos
#end index will be last house pos
#k will be mailboxes in the group
def allocate_mailboxes(start: int, end : int, k : int): 

    #Base case: if there is one mailbox, place it at the median house (hint from LC) 
    if k == 1: 
        mid_index = int(st.median([start, end]))
        total_dist = 0
        for i in range(start, end + 1): 
            total_dist += (abs(houses_pos[i] - houses_pos[mid_index])) #adds total distance from each house to mailbox
        return total_dist
    
    #Another base case: if there is a mailbox for every house in the group, then total distance will be 0
    if k == (end - start) + 1:
        return 0

   

    total_dist = 10000000

    #need to break houses into k subgroups. Each subgroup gets one mailbox
    for i in range (start, end): #tries every possible partition of the houses  
        inst_dist = allocate_mailboxes(start, i, 1) + allocate_mailboxes(i+1, end, k-1)
        #replace total distance if instant distance is 
        if inst_dist < total_dist: 
            total_dist = inst_dist

        '''
        each time the loop runs, the program partitions the houses list. the idea is to make two groups: the first group is given one mailbox (first 'allocate_mailboxes') and the second group is given
            the rest of the mailboxes. Recursion is used to continue partitioning the second group over and over until the mailboxes for that group = 1 (therefore recurses k-1 times). When the mailboxes
            for the second group == 1, the method finds the median house in the group and places the mailbox there.  
        '''

        #old code to show the partition
        #   group1 = houses_pos[start:i]
        #   group2 = houses_pos[i:end]
        #   print(group1, group2)
        #form k-1 groups out of group2

    return total_dist

print(allocate_mailboxes(0, len(houses_pos) - 1, k))
