import math

lower_bound = int(input("Enter a lower bound: "))
upper_bound = int(input("Enter an upper bound: "))
prime_numbers = [2, 3]
i = lower_bound

if(lower_bound<1):
    print("Your number is invalid. Please try again.")

elif(1<=lower_bound<3): 
    print(f"{n}st Prime number is : {prime_numbers[n-1]}")

elif (lower_bound>2):
    prime_numbers = []
    cont = True
    while (cont == True):
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

        if i == upper_bound:
            cont = False
    print(prime_numbers)
    
        
            
        
