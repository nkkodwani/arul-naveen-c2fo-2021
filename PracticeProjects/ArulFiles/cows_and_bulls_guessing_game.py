#COWS AND BULLS GUESSING GAME: Excercise 18 from practicepython.org

import random

n = random.randint(1000, 2000) #change to (1000, 9999)
n_str = str(n)

guessed = False
count = 0

cows = int()
bulls = int()

print("\nWelcome to the Cows and Bulls Game! Guess a four-digit number. ")
print("\tCorrect guessed digit = 'cow'; Incorrect guessed digit = 'bull.'")

while not guessed:
    count += 1
    inp = (input("\nPlease input a four-digit number: "))
    bd = str(inp)
    index_bd = int()
    if len(bd) == 4:
        for i in range(0, 4):
            if bd[index_bd] == n_str[index_bd]: 
                cows += 1
            else: 
                bulls += 1
            index_bd += 1
        if cows == 4:
            guessed = True
        else: 
            print(f"\t{cows} cows, {bulls} bulls")
            cows = 0
            bulls = 0
            index_bd = 0
    else:
        print("Please enter a valid number.")

print(f"\nCongratulations! You guessed {n} in {count} tries!")

