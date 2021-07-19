#fibbonaci
count = int(input("Enter amount of fibonacci numbers: "))
fibb = [1, 1]
length = 2
cont = True

if count <=2:
    if count <1:
        print("Enter a number >= 1.")
    elif count == 1:
        fibb == [1]
    elif count == 2: 
        print(fibb)

elif count > 2:
    while cont == True:
        new_fibb = int(fibb[-1] + fibb[-2])
        fibb.append(new_fibb)
        length = len(fibb)
        if length == count:
            cont = False
            break
    print(fibb)

