#doesnt work right now
#I basically tried fixing it once, but gave up halfway through, so its a mess right now
#This basically wont be touched at all, and is just here to refer back to what I did before and what went wrong
b = False
import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#card class: each card has its own suit and rank values
class Card:    
    def __init__(self,suit,rank):

        #have to decide on how to print stuff. Do I keep the __str__ or do I make separate methods to return values of suits and ranks
        #If i inted to go further with this, its probably better to use methods. Gives more manuverability and is easier to understand
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of " + self.suit



#deck class: contains a list of all cards left in the deck, as well as a way to shuffle and deal them. __str__ can be ignored.
class Deck:
    
    def __init__(self,suits,ranks):
        self.deck = []   # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        return str(self.deck)
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop(0)



#the most annoying class: the hand class. I want to be able to make up to 4 people playing , so that needs to be kept in mind
#when coding this
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        self.count = 0
    #straightforward, a list of all your cards, a count of how many aces, and a value. count is a stupid idea and definitely not important
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        return str(self.cards[-1]), self.value
    #choose whether an ace is a 11 or 1. This gave me a HUGE headache back then, and im gonna revamp the entire system here
    #honestly makes me sick just trying to figure out how I came up with this mess
    def adjust_for_ace(self):
        self.count = 0
        for card in self.cards:
            self.count += 1
            if card.rank == 'Ace':
                self.aces += 1
                card.rank = 'Ace '
                
        if self.aces >= 1:
            print("your cards are worth(when your new ace = 11): " + str(self.value))
            while True:
                aceInput = input("would you like your ace to be worth 1 or 11(input 1 or 11)")
                if aceInput == '1':
                    self.value -= 10
                    self.aces -= 1
                    print("your cards are now worth: " + str(self.value))
                    break
                elif aceInput == '11':
                    self.aces -= 1
                    break
                else:
                    print("that doesnt seem right!")
                    continue


#ah, the easy part. I remember this working like a charm, so I might just copy it in directly with a few changes
#have to make sure the numbers stay between rounds, and maybe add a function to add to your chip total. Basically have an option to either:
#end the game as a whole, start another round, either add an option to add/subtract chips or have the person with the most chips after
# a certain amount of time to win, or maybe have a domination-esque thing where you need to have every chip on the board to win. 
#each round needs to start by taking bets from all the players(including the CPUs), and calculating the new number of chips each person
#has after subtracting their bets and storing them in a new value(in case they win).
class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input(addi it in the parameters)
        self.bet = 0
    def win_bet(self): 
        self.total += self.bet
    def lose_bet(self):
        print("You lost " + self.bet + "chips")


def take_bet(chips):
    print("number of chips = " + str(chips.total))
    while True:
        try:
            chips.bet = int(input('Enter your bet: '))
            if chips.bet > chips.total:
                print("Amount bet must be below total number of chips")
                continue
                
        except:
            print("Oops! there was a problem!")
        else:
            print("betting " + str(chips.bet) + " chip(s)" )
            chips.total -= chips.bet
            print("number of chips(new) = " + str(chips.total))
            break

def hit(deck,hand):
    if hand.value < 21:
        hand.add_card(deck.deal())
    if hand.value == 21:
        print("you already have 21!")
        playing = False

def hit_or_stand():
    global playing  # to control an upcoming while loop
    hitStand = input('Hit or Stand?: ')
    while hitStand.lower() != 'hit' and hitStand.lower() != 'stand':
        hitStand = input('Hit or Stand?: ')
    if hitStand.lower() == 'hit':
        playing = True
        return True
    else:
        playing = False
        return False

def show_some(player,dealer):
    
    print(dealer[1:])
    
    
def show_all(player,dealer):
    
    print(player.cards)
    print(player.value)

def player_wins():
    print("YOU WIN!")
    
def dealer_busts():
    print("YOU WIN THE DEALER BUSTED")
    
def dealer_wins():
    print("YOU LOSE! I guess he got lucky.")
    
def push():
    pass

b = True

def printcard(hand,who):
    e = 0
    print(who + "'s hand: ", end = '')
    if who  == "player":
        e = 0
    elif who == "CPU":
        e = 2
        print("HIDDENCARD, ", end = '')
    else:
        pass
    while e < len(hand.cards):

            print(hand.cards[e] + " of " + hand.cards[e + 1] , end = "")
            e += 2
            if e == len(hand.cards): pass 
            else: print(", ", end = "")
            
    print("\n")
    if who == "player":
        print(who + "'s card value: " + str(hand.value))
def check21(hand):
    if hand.value >= 21:
        return False
    else:
        return True
while True:
    print("hello and welcome to blackjack. By: Nebil Ozer")
    print("You start with 100 chips. you gain chips at a 1:1 rate, and can choose to quit after any round.")
    phand = 0
    dhand = 2
    # Create & shuffle the deck, deal two cards to each player
    import random

    suits = ('Hearts','Diamonds','Spades','Clubs')
    ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}

    playing = True
    deck = Deck(suits,ranks)
    deck.shuffle()
    dealer_hand = Hand()
    player_hand = Hand()
    
    
    
        
        
    # Set up the Player's chips
    
    # Prompt the Player for their bet
    pchips = Chips()
    take_bet(pchips)
    
    # Show cards (but keep one dealer card hidden)
    hit(deck,player_hand)
    hit(deck,player_hand)
    hit(deck,dealer_hand)
    hit(deck,dealer_hand)
    printcard(dealer_hand,"CPU")
    printcard(player_hand,"player")
    player_hand.adjust_for_ace()
    while playing:  
        
        # Prompt for Player to Hit or Stand
        if check21(player_hand):
            if hit_or_stand():
                hit(deck,player_hand)
                player_hand.adjust_for_ace()
                print(b)
        elif player_hand.value == 21:
            print("YOU WON! got 21!")
            b = False
            break
        else:
            print("YOU LOST! BUSTED!")
            b = False
            print(b)
            break
        # Show cards (but keep one dealer card hidden)
        
        printcard(dealer_hand,"CPU")
        printcard(player_hand,"player")
    print("-----DEALER TURN-----")
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if b:
        
        while dealer_hand.value < 17:
            printcard(dealer_hand, "CPU ")
            print("dealer hits!")
            hit(deck,dealer_hand)
    
        
        # Show all cards
    if b:
        printcard(dealer_hand, "CPU ")
        print("value of CPU hand: ", dealer_hand.value)
        # Run different winning scenarios
        if dealer_hand.value <= 21:
            if player_hand.value > dealer_hand.value:
                print("YOU WIN! GG")
                player += pchips.bet*2
            elif player_hand.value < dealer_hand.value:
                print("You lost. guess he got lucky")
                
            else:
                print("TIE")
                player += pchips
                
    # Inform Player of their chips total 
    print("chips total: ", pchips.total)
    # Ask to play again
    if input("play again? y/n") == "n":
        break