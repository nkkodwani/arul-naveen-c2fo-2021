######
#PROBLEM:
# Determine number of steps to change one 32 bit unsigned int to another
# Example: 100 --> 101 takes one step
# Example 2: 10001 --> 11111 takes three steps
######

def binaryEditDP(num1, num2):
    
    m = '{:032b}'.format(num1) #converts num1 to binary
    n = '{:032b}'.format(num2 )# converts num2 to binary
    z = num1 ^ num2 #ex-or operator counts differnces: each different digit becomes a '1' in z
    count_diff = 0
    while z != 0:
        if (z & 1): #if digit in last place of z has a 1 in it: ++ to count_differences variable
            count_diff += 1
        z = z >> 1 #right shift z to check next digit
    return count_diff

num1 = 9
num2 = 548 #Example 2: 10001 --> 1111 takes three steps

print('{:032b}'.format(num1))
print('{:032b}'.format(num2))
print(binaryEditDP(num1, num2))