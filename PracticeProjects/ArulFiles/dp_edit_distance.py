###########
# EDIT DISTANCE
###########
import numpy as np

def edit_dist(str1, str2):
    m = len(str1)
    n = len(str2) 
    if m == 0:
        return n
    if n == 0:
        return m
    a1 = np.zeros((m + 1, n + 1)) #create empty array 
    # a1 = np.zeros([0 for x in range(n + 1)] for x in range(m + 1))

    for i in range(m + 1): #vertical indexing through str1
        for j in range(n + 1): #horizontal indexing through str2
            if i == 0: #first row
                a1[i][j] =  j# fill in with length of str2
            elif j == 0: #first column
                a1[i][j] = i #fill in with length of str1 
            # these previous two operations represent # of ops. 
            # creating the string from empty character
            elif str1[i-1] == str2[j-1]: 
                a1[i][j] = a1[i-1][j-1]
            # if the two characters on index are equal, then 
            # ignore and use moves of prev. character (diag)
            elif str1[i-1] != str2[j-1]:
                a1[i][j] = 1 + min( a1[i-1][j], #left = delete char
                                a1[i-1][j-1], #diag = replace char
                                a1[i][j-1] #up = insert a char
                                ) # +1 to perform insert/replace/del
        
    return a1, a1[i][j] #returns the final spot in array

    
str1 = str(input("String 1: "))
str2 = str(input("String 2: "))
print( edit_dist(str1, str2))

# print(f"Editing {str1} to {str2} would take {operations} operations.")


            
