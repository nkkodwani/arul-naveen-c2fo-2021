import random
import pandas as pd

exit = False
count_data = [int(),int(),int(),int(),int()] #will store count data for each game
game = 0 #counts game number

while exit == False and game < 5: #stops if user types 'exit' or if game5 is completed

    n = random.randint(1, 100)
    count = 0
    print("\nINSTRUCTIONS:\n\tGuess the number from 1 to 100, or type 'exit' to finish.\n\tThe game will restart every time the number is guessed.")
    print(f"\tMaximum of five games. You have {5-game} games remaining.")
    game+=1
    cont = True

    while cont == True:
        count += 1
        guess = (input("Guess a number between 1 and 100: "))
        if (str(guess)).lower() == 'exit': #stops game 
            exit = True
            break
        elif int(guess) == n:
            print(f"\nCorrect!\n\tIt took you {count} tries to guess {n}.")
            count_data[game-1] = count #stores the number of guesses into the count_data list
            cont = False
        elif int(guess) < n: 
            print("Your guess is too low. ")
        elif int(guess) > n: 
            print("Your guess is too high. ")
        else:
            print("Enter a valid guess")

print("\tYour five games are up! Here is your data:\n")

#basic statistics testing
data = {'Games Played' : [1, 2, 3, 4, 5], 
    'Guesses' : [count_data[0], count_data[1], count_data[2], count_data[3], count_data[4]]
    }
df = pd.DataFrame(data, columns= ['Games Played', 'Guesses']) #creates dataframe out of game data
print(f"{df}\n")
print(f"{df['Guesses'].describe()}\n")
download_data = str(input("Download data as .csv? (y/n): "))
if download_data.lower() == 'y':
    df.to_csv('~/Desktop/PythonWork/guessing_game_data/game_data.csv')
    df['Guesses'].describe().to_csv('~/Desktop/PythonWork/guessing_game_data/game_data_stats.csv')
print("Thanks for playing!\n")
