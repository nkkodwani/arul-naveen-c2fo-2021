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
    k = 1 : put mailbox in median (given by leetcode hint)
    partition!
    break houses into k groups and store results
        from leetcode discussion: form one group, then form k-1 groups with remaining elements
    to do this: vvvvvv

    need to form k total groups: 
    create one group: length is maximum of (len(houses) - (k-1)) 
    from k-1 groups out of remaining houses not in group1




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
#right now this is kinda useless


#start index will be first house pos
#end index will be last house pos
def allocate_mailboxes(start: int, end : int, k : int): #start and end are indexes in the houses_pos list

    # total_dist = 1000000

    #Base case: if there is one mailbox, place it at the median house (hint from LC) 
    if k == 1: 
        mid_index = int(st.median([start, end]))
        total_dist = 0
        for i in range(start, end + 1): 
            total_dist += (abs(houses_pos[i] - houses_pos[mid_index]))
        return total_dist
    
    #if there is a mailbox for every house in the group, then 
    if k == (end - start) + 1:
        return 0

    #need to break houses into k subgroups
    #first create a group1

    total_dist = 10000000

    for i in range (start, end): #+2 because we want (len(houses) - (k-1)) to be included in the range
        total_dist = min(total_dist, allocate_mailboxes(start, i, 1) + allocate_mailboxes(i, end, k-1))

        '''group1 = houses_pos[0:i]
        group2 = houses_pos[i:]
        print(group1, group2)
        #form k-1 groups out of remaining houses not in group1'''

    return total_dist

print(allocate_mailboxes(0, len(houses_pos) - 1, k))
