######
#PROBLEM:
# Determine number of steps to change one 32 bit unsigned int to another
# Example: 100 --> 101 takes one step
# Example 2: 10001 --> 11111 takes three steps
######
import numpy as np

def binaryEditDP(num1, num2):
    
    m = '{:032b}'.format(num1) #bin(num1)
    n = '{:032b}'.format(num2 )# bin(num2)
    a = str(m)
    b = str(n)
    i = 0
    change = 0

    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    if b == a:
        return 0

    while i < 32:
        if a[i] != b[i]:
            change += 1
        i += 1

    return change

num1 = 8972345902943
num2 = 2430895092435
num1_bit = '{:032b}'.format(num1)
num2_bit = '{:032b}'.format(num2)

print(binaryEditDP(num1, num2))


#Trying to do binary edit problem using an array
a1 = np.empty((32, 32))
print(a1)