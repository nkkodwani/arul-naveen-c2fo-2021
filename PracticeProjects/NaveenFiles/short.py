import random

Card_Deck = {
    1 : tuple([2, 'spades']),
    2 : tuple([3, 'spades']),
    3 : tuple([4, 'spades']),
    4 : tuple([5, 'spades']),
    5 : tuple([6, 'spades']),
    6 : tuple([7, 'spades']),
    7 : tuple([8, 'spades']),
    8 : tuple([9, 'spades']),
    9 : tuple([10, 'spades']),
    10 : tuple([11, 'spades']),
    11 : tuple([12, 'spades']),
    12 : tuple([13, 'spades']),
    13 : tuple([14, 'spades']),
    14 : tuple([2, 'hearts']),
    15 : tuple([3, 'hearts']),
    16 : tuple([4, 'hearts']),
    17 : tuple([5, 'hearts']),
    18 : tuple([6, 'hearts']),
    29 : tuple([7, 'hearts']),
    20 : tuple([8, 'hearts']),
    21 : tuple([9, 'hearts']),
    22 : tuple([10, 'hearts']),
    23 : tuple([11, 'hearts']),
    24 : tuple([12, 'hearts']),
    25 : tuple([13, 'hearts']),
    26 : tuple([14, 'hearts']),
    27 : tuple([2, 'clubs']),
    28 : tuple([3, 'clubs']),
    29 : tuple([4, 'clubs']),
    30 : tuple([5, 'clubs']),
    31 : tuple([6, 'clubs']),
    32 : tuple([7, 'clubs']),
    33 : tuple([8, 'clubs']),
    34 : tuple([9, 'clubs']),
    35 : tuple([10, 'clubs']),
    36 : tuple([11, 'clubs']),
    37 : tuple([12, 'clubs']),
    38 : tuple([13, 'clubs']),
    39 : tuple([14, 'clubs']),
    40 : tuple([2, 'diamonds']),
    41 : tuple([3, 'diamonds']),
    42 : tuple([4, 'diamonds']),
    43 : tuple([5, 'diamonds']),
    44 : tuple([6, 'diamonds']),
    45 : tuple([7, 'diamonds']),
    46 : tuple([8, 'diamonds']),
    47 : tuple([9, 'diamonds']),
    48 : tuple([10, 'diamonds']),
    49 : tuple([11, 'diamonds']),
    50 : tuple([12, 'diamonds']),
    51 : tuple([13, 'diaamonds']),
    52 : tuple([14, 'diamonds'])
}

'''item = list(Card_Deck.keys())
print(item)
random.shuffle(item)
for key in item:
   ((key, ':', Card_Deck[key]))
   
print((key, ':', Card_Deck[key]))
#d.append[key, ':', Card_Deck[key]))
#d[key].append(':', Card_Deck[key])
player1 = Card_Deck[0:int(len(Card_Deck)/2)]
player2 = Card_Deck[0:int(len(Card_Deck)/2):len(Card_Deck)]

player1 = dict(list((key, ':', Card_Deck[key].items))([len(key, ':', Card_Deck[key])//2]))

player2 = dict(list((key, ':', Card_Deck[key].items))([len(key, ':', Card_Deck[key])//2]))
player1 = (list(Card_Deck.items())([len(Card_Deck)//2]))
player1 = dict(player1)

player2 = (list(Card_Deck.items())([len(Card_Deck)//2]))
player2 = dict(player2)
print(player1)

from itertools import islice
inc = iter(Card_Deck.items())
res1 = dict(islice(inc, len(Card_Deck) // 2)) 
res2 = dict(inc)

print("The first half of dictionary : " + str(res1))
print("The second half of dictionary : " + str(res2))'''
import random 
from itertools import islice
def shuffleAndSplitDeck(self, Card_Deck, p1_deck, p2_deck): #naveen will do this
    #shuffle cards in the deck
    item = list(Card_Deck.keys())
    random.shuffle(item)
    Card_Deck = {item[i] : Card_Deck[item[i]] for i in range(0, 51)}
    #divide shuffled list into 26 cards per player
    inc = iter(Card_Deck.items())
    p1_deck = dict(islice(inc, len(Card_Deck) // 2))
    p2_deck = dict(inc)
    print(Card_Deck)
    print()
    print(p1_deck)
    print()
    print(p2_deck)

print(shuffleAndSplitDeck)