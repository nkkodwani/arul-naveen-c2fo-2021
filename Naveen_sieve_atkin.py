import math

n = int(input("Enter a number: "))
prime_numbers = [2, 3]
i = 3
my_list = [2, 3, 5]

if(n<1):
    print("Your number is invalid. Please try again.")

elif(1<=n<2):
    print(f"{n} : {prime_numbers[n-1] and [n]}")

elif (n>2):
    while (True):
        i += 1
        status = True
        #for j in range(2, int(math.sqrt(i) + 1)): #sqrt makes answer inaccurate
            #adi note - instead of setting sqrti, make it x * x < i
        for j in range(2, int(i/2 + 1)):
            if (i % j == 0):
                status = False
                break

        if (status == True): #if the number passes the above test, it is prime. we add the number to our prime numbers list
            prime_numbers.append(i)

