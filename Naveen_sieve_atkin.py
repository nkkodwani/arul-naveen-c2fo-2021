n = int(input("Enter a number: "))
prime_numbers = [2, 3, 5]
value = True
#num is prime if it is not divisible by anything other than 1 and itself
if n <= 1:
    print("Invalid input choose and number greater than 1")
#def prime_values(n):
if n == 1:
        print(2)
if n == 2:
    print(2, 3) #chec

i = 3

while (value == True): #arul did this for nave
    status = True
    i+=1
    for j in range(2, int(i/2 + 1)):
        if (i % j == 0):
            status = False
    if status == True:
        prime_numbers.append(i)
    if i == n:
        value = False
        break

print(prime_numbers)
