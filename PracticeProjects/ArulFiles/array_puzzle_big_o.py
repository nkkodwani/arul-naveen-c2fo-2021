#practice project - puzzle:
#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)). bubble? quick sort? insertion? merge? 

'''
a function w/ log time: 
- the choice of the next elemenet on which to perform some action is one of several possibilities
- only one will need to be chosen

pseudocode:
- get lengths of each list
- combine the sorted lists
- get length of new list
- sort by dividing length by 2 and picking the median value; create a case for even/odd lengths
- print median
'''

#initialize nums1 and nums2; already sorted
nums1 = [2, 3, 4, 4, 5, 6, 7, 9, 10, 12, 14, 15, 16, 18, 18, 20, 21, 24, 25, 26, 29]
nums2 = [0, 1, 4, 5, 5, 7, 9, 11, 12, 14, 14, 15, 16, 18, 19, 21, 24, 28, 32, 32, 33]

a = 0 #a and b will be used to index through the list and compare
b = 0

m = len(nums1) - 1
n = len(nums2) - 1
combined_list = [] #left empty, will append from nums1 and nums2

#SORT: compare a with b. add the smaller to the combined list
while a < m and b < n: 
    if nums1[a] < nums2[b]:
        combined_list.append(nums1[a])
        a+=1
    elif nums1[a] > nums2[b]:
        combined_list.append(nums2[b])
        b+=1
    elif nums1[a] == nums2[b]:
        combined_list.append(nums1[a])
        combined_list.append(nums2[b])
        a+=1
        b+=1
#runtime complexity: O(n)? How do I get this to O(log(n))

#now that the combined_list is sorted, the next step is to find the median

print(combined_list) 





