'''make a class for cards data storage and for player/comp to play card game war 
1. player class --> constructor for playername, some data, comp/human, 
    methods: ask for input 
            play card
2. game class --> 
    methods: start game
            shuffle deck
            play function (compare)
3. card dictionary
'''
Card_Deck = {
    1 : [2, 'spades'],
    2 : [3, 'spades'],
    3 : [4, 'spades'],
    4 : [5, 'spades'],
    5 : [6, 'spades'],
    6 : [7, 'spades'],
    7 : [8, 'spades'],
    8 : [9, 'spades'],
    9 : [10, 'spades'],
    10 : [11, 'spades'],
    11 : [12, 'spades'],
    12 : [13, 'spades'],
    13 : [14, 'spades'],
    14 : [2, 'hearts'],
    15 : [3, 'hearts'],
    16 : [4, 'hearts'],
    17 : [5, 'hearts'],
    18 : [6, 'hearts'],
    29 : [7, 'hearts'],
    20 : [8, 'hearts'],
    21 : [9, 'hearts'],
    22 : [10, 'hearts'],
    23 : [11, 'hearts'],
    24 : [12, 'hearts'],
    25 : [13, 'hearts'],
    26 : [14, 'hearts'],
    27 : [2, 'clubs'],
    28 : [3, 'clubs'],
    29 : [4, 'clubs'],
    30 : [5, 'clubs'],
    31 : [6, 'clubs'],
    32 : [7, 'clubs'],
    33 : [8, 'clubs'],
    34 : [9, 'clubs'],
    35 : [10, 'clubs'],
    36 : [11, 'clubs'],
    37 : [12, 'clubs'],
    38 : [13, 'clubs'],
    39 : [14, 'clubs'],
    40 : [2, 'diamonds'],
    41 : [3, 'diamonds'],
    42 : [4, 'diamonds'],
    43 : [5, 'diamonds'],
    44 : [6, 'diamonds'],
    45 : [7, 'diamonds'],
    46 : [8, 'diamonds'],
    47 : [9, 'diamonds'],
    48 : [10, 'diamonds'],
    49 : [11, 'diamonds'],
    50 : [12, 'diamonds'],
    51 : [13, 'diaamonds'],
    52 : [14, 'diamonds']
}

class Player:
    #create a class for the Player
    def __init__(self, name, comp):
        self.name = name
        self.comp = comp
    
    def computerPlaying(self, comp):
        if comp == True:
            print("A computer is playing.")
        else:
            print("A human is playing.")

class Game:
    #class for all functoins in game
    def __init__ (Card_Deck):  
        print()

    def startGame(self):
        print()

    def shuffleDeck(self, deck):
        print()