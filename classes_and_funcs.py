#This will be used to make each card and give it a value. Very useful, so I directly copied it over

import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

#I'm gonna use get methods for suits and ranks, as that way just comes more naturally to me, and makes a lot more sense in the
#long run.

#i'm pretty happy about how this works, and the Get methods will definitely help a lot more than it seems at first
#python is pretty wonky about fields, so I dont even want to bother with dealing with that when I can just have a get func
class Card:
    #initialize a card by giving it a suit and a rank, 10/8/20:include the value for easier changing of it in the 1/11 aces thing
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        if rank == "Ace":
            self.isace = True
        else:
            self.isace = False
        self.value = values[rank]
    #func that gives the full name for convenience sake
    def cardName(self):
        return self.rank + " of " + self.suit

    #the get funcs
    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank
    
    def getValuec(self):
        return self.value
    
    def acesetupc(self,oneeleven):
        if oneeleven == 1:
            self.value = 1
            self.isace = False
            return False
        elif oneeleven == 11:
            self.value = 11
            self.isace = False
            return False
        


#The top of the deck is actually the end of the list. Deck class will be all of the functions having to do with
#how the players interact with the deck throughout the game
class Deck:
#Initialize Deck by giving it an empty list as the "deck". This will be changed by adding and taking away from it. 
    def __init__(self):
        self.deck = []
#shuffle the current deck
    def shuffle(self):
        random.shuffle(self.deck)
#add a card to the "top" of the deck
    def addCard(self,card):
        self.deck.append(card)
#draw a card from the "top" of the deck 
    def drawCard(self):
        return self.deck.pop()
#resets the deck for a new game (called in the beginning of each game)
    def reset(self):
        for suit in suits:
            for rank in ranks:
                self.addCard(Card(suit,rank))
        self.shuffle()
# this last one is just for debugging
    def showDeck(self):
        for x in self.deck:
            print(x.cardName(),end=" ||| ")

#basically the class for all the things each player can actually do and see. Definitely gonna add more to this later as the need
#arises
class Hand:
    #initialize the hand with an empty list where the cards will go, and a number containing the full value of those cards
    def __init__(self,player):
        self.hand = []
        self.player = player
    #draw one card and add it to the hand
    def draw(self,card):
        self.hand.append(card)
    #print out the value of the total 
    def getValueh(self):
        total = 0
        for card in self.hand:
            total += card.getValuec()
        return total
    def clearhand(self):
        self.hand = []
    #print out all the remaining cards (basically a copy of the deck method's one but you return it instead of printing)
    def showHand(self):
        handstr = "||| "
        for x in self.hand:
            handstr += x.cardName() + " ||| "
        return handstr
    def acesetuph(self,card):
        if card.isace == True:
            a = True
            while a:
                try:
                    a = card.acesetupc(int(input(self.player + ", would you like your ace to be 1 or 11?(scoreboard shows 11)")))#will change the question later
                except:
                    print("Invalid input. Try again \n")
        




#10/8/20: I have decided to move the 1/11 for aces over to the card class instead, where depending on what you choose, the value
#of the card is directly changed to reflect your decision.
""" Debugging for first section
h = Hand()
d = Deck()
d.reset()
h.draw(d.drawCard())
h.draw(d.drawCard())
print(h.showHand())
print(h.getValueh())
"""
#this class represents the total number of chips in the hand of a particular player
class Chips:
    #initialize the chips and put a cap on the number of chips possible
    def __init__(self,total,player):
        self.player = player
        if total <= 9999:
            self.total = total  # This can be set to a default value or supplied by a user input(addi it in the parameters)
        else:
            self.total = 9999
        self.bet = 0
    #get methods
    def getTotal(self):
        return self.total
    
    def getBet(self):
        return self.bet

    #winning or losing a bet
    def win_bet(self,amtwon): 
        self.total += amtwon

    def lose_bet(self):
        print("You lost " + str(self.bet) + "chips")
        self.total -= self.bet

    #making a bet. had to use try/except in order to make sure that people cant put in werid inputs
    def make_bet(self):
        #ok so need to figure out how to have the first one act similarly to the rest. Basically, if you
        #put in a weird input the first time, it says you dont have that many chips. I could do it with if/else, but thats 
        #annoying as hell. Just brainstorm for now
        print(self.player + " Current # of chips: " + str(self.getTotal()))
        switch = False
        self.bet = 10000000
        try:
            self.bet = int(input(self.player + ", what is your bet?"))
        except:
            print("\ninvalid input: please try again!\n")
            switch = True
        while self.bet > self.total:
            try:
                if not switch:
                    print("\nyou dont have that many chips!\n")
                else:
                    switch = False
                self.bet = int(input(self.player + ", what is your bet?"))
            except:
                print("\ninvalid input: please try again!\n")
                switch = True

        
#just testing the chips class
"""
p1chips = Chips(100000,"player1")
p1chips.make_bet()
print(p1chips.getBet())
p1chips.win_bet()
print(p1chips.getTotal())
"""

#now, its time to get the functions done. These functions are basically the "actions" that the player can take on their turn,
#including hitting, standing, and bust

def hit(deck,hand):
    hand.draw(deck.drawCard())
#testing the hit class and multiple hands using one deck
"""
h = Hand()
h2 = Hand()
d = Deck()
d.reset()
hit(d,h)
hit(d,h2)
print(h.showHand())
print(h2.showHand())
"""

#only after coding this did i realize it would be so much easier to just make 
# it so that if there isnt a value for a player, it just prints - instead :facepalm

#Player class in order to link the Chips of a player to their Cards.
class Player:
    def __init__(self,hand,chips,player,null):
        self.null = null
        self.hand = hand
        self.chips = chips
        self.player = player
    def getname(self):
        return self.player



    
    
