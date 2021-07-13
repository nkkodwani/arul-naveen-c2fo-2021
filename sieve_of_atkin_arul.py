

limit = int(input("Please input a limit: "))
prime_numbers = [2, 3]
cont = True

if limit <= 3: 
    if limit == 1:
        print("There are no prime numbers <= than 1")
    elif limit == 2:
        print(prime_numbers[0])
    elif limit == 3:
        print(prime_numbers)

n = 3

while(cont == True):
    prime = True
    if n == limit:
        for d in range (2, int(n/2 + 1)):
            if (n % d == 0):
                prime = False
                break
        if prime == True:
            prime_numbers.append(n)
        cont = False
    else:
        n+=1
        for d in range (2, (int(n/2 + 1))): #this line can be optimized for runtime
            if (n % d == 0):
                prime = False
                break
        if prime == True:
            prime_numbers.append(n)

print(prime_numbers)

'''
pseudocode:
- ask user for limit
- initialize list with first 2 primes (if limit is less than that, make conditions)
- create variable (n) that will increase and if prime will be added to list 
- make sure list stops growing when n crosses limit
    - if n = limit: check if n is prime then add to list; stop loop
    - else: increase n, check if n is prime then add to list if yes, repeat loop   
'''




