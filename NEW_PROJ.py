
#This will be used to make each card and give it a value. Very useful, so I directly copied it over
"""
import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
"""
#I'm gonna use get methods for suits and ranks, as that way just comes more naturally to me, and makes a lot more sense in the
#long run.

#i'm pretty happy about how this works, and the Get methods will definitely help a lot more than it seems at first
#python is pretty wonky about fields, so I dont even want to bother with dealing with that when I can just have a get func
class Card:
    #initialize a card by giving it a suit and a rank
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    #func that gives the full name for convenience sake
    def cardName(self):
        return self.rank + " of " + self.suit

    #the get funcs
    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank

y = Card("Hearts","Two")
print(y.cardName())