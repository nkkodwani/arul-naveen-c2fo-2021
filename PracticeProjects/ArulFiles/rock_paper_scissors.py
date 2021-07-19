p1 = (input("Player 1, please input your play: "))
p2 = (input("Player 2, please input your play: "))

if p1.lower() == 'rock':
    if p2.lower() == 'scissors':
        print("Player 1 wins")
    elif p2.lower() == 'paper': 
        print("Player 2 wins")
    elif p2.lower() == 'rock':
        print("Tie!")
    else:
        print('enter valid input')

elif p1.lower() == 'scissors':
    if p2.lower() == 'scissors':
        print('Tie! Play again')
    elif p2.lower() == 'paper':
        print('Player 1 wins')
    elif p2.lower() == 'rock':
        print('Player 2 wins')
    else:
        print("enter valid input")

elif p1.lower == 'paper': 
    if p2.lower() == 'scissors':
        print("Player 2 wins")
    elif p2.lower() == 'rock':
        print("Player 1 wins")
    elif p2.lower() == 'paper': 
        print('Tie! Play again')
    elif p2.lower() != 'paper' or 'rock' or 'scissors':
        print("enter valid input")

else:
    print("enter valid input")

