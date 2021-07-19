'''make a class for cards data storage and for player/comp to play card game war 
1. player class --> constructor for playername, some data, comp/human, 
    methods: ask for input 
            play card
2. game class --> 
    methods: start game
            shuffle deck
            play function (compare)
3. card dictionary

class Player:
    #create a class for the Player
    def __init__(self, name):
        self.name = str(input("Please input your name: "))
    
    def computerPlaying(self, comp):
        if comp == True:
            print("A computer is playing.")
        else:
            print("A human is playing.")''' #the game will be human vs rand. comp. this class is no longer needed

from itertools import islice
import random

class Game:

    #class for all functions in game
    def __init__ (self, Card_Deck, p1_deck, p2_deck): 
        self.Card_Deck = dict(Card_Deck)
        self.p1_deck = dict(p1_deck)
        self.p2_deck = dict(p2_deck)
        

    def createGame(self, Card_Deck):
        #initialize the card deck
        return(Card_Deck)

    
    def shuffleAndSplitDeck(self, Card_Deck, p1_deck, p2_deck): 
        #shuffle cards in the deck
        item = list(self.Card_Deck.keys())
        random.shuffle(item)
        self.Card_Deck = {item[i] : Card_Deck[item[i]] for i in range(0, 51)}
        #divide shuffled list into 26 cards per player
        inc = iter(self.Card_Deck.items())
        self.p1_deck = dict(islice(inc, (len(self.Card_Deck)+1) // 2)) #how do i save these variables? are these instance variables?
        self.p2_deck = dict(inc)
        return self.Card_Deck, p1_deck, p2_deck 
    
    def play(p1_deck, p2_deck):
        #reveal the first card in each player's deck
        
        return

    def compare(self):
        #if card_p1 = card_p2
        return


    