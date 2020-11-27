from classes_and_funcs import Deck
from classes_and_funcs import Card
from classes_and_funcs import Hand
from classes_and_funcs import Chips
from classes_and_funcs import hit
from classes_and_funcs import Player

def turn(player):
    if player.null:
        printUI(int(numplay))
        player.hand.acesetuph(player.hand.hand[0])
        player.hand.acesetuph(player.hand.hand[1])
        while True:
            printUI(int(numplay))
            print(player.getname().upper() + " TURN\n")
            player.hand.acesetuph(player.hand.hand[-1])
            print("Current bet: " + str(player.chips.getBet()),end="\n\n")
            print("Current card total: " + str(player.hand.getValueh()), end="\n\n")
            print("Current cards: " + player.hand.showHand(), end = "\n\n")
            p2
            if player.hand.getValueh() < 21:
                hitorstand = input(player.getname() + ", would you like to hit or stand?(h/s)(anything else will defualt to hit)")
                if hitorstand.lower() == "s":
                    clear()
                    print(player.getname() + " has chosen to stand. ", end = "\n\n") 
                    if dealerturn:
                        input("All players have gone, enter to finish game")
                    else:
                        input(order[order.index(player.getname())+1]  + ", prepare to play(enter).")
                    break
                else:
                    hit(deck,player.hand)
            elif player.hand.getValueh() == 21:
                print(player.getname() + " HAS HIT 21!!",end = "\n\n") 
                if dealerturn:
                    input("All players have gone, enter to finish game")
                else:
                    input(order[order.index(player.getname())+1]  + ", prepare to play(enter).")
                break
            else:
                print(player.getname() + " HAS BUSTED! GG! ",end = "\n\n")
                if dealerturn:
                    input("All players have gone, enter to finish game")
                else:
                    input(order[order.index(player.getname())+1]  + ", prepare to play(enter).")
                break



def printUI(numplayers):
    clear()
    if not dealerturn:
        dealer = str(p1.hand.hand[0].getValuec()) + """ + ???""" 
    else:
        dealer = str(p1.hand.getValueh())
    if numplayers == 2:
        print(
        """
        ---------------------------------------------------------------------
        | DEALER TOTAL: """ + dealer + """ | P2 TOTAL: """ + str(p2.hand.getValueh()) + """ | P3 TOTAL: - | P4 TOTAL: - |
        ---------------------------------------------------------------------
        """)
    elif numplayers == 3:
        print(
        """
        ---------------------------------------------------------------------
        | DEALER TOTAL: """ + str(p1.hand.hand[0].getValuec()) + """ + ??? | P2 TOTAL: """ + str(p2.hand.getValueh()) + """ | P3 TOTAL: """ + str(p3.hand.getValueh()) + """ | P4 TOTAL: - |
        ---------------------------------------------------------------------
        """)
    elif numplayers == 4:
        print(
        """
        ---------------------------------------------------------------------
        | DEALER TOTAL: """ + str(p1.hand.hand[0].getValuec()) + """ + ??? | P2 TOTAL: """ + str(p2.hand.getValueh()) + """ | P3 TOTAL: """ + str(p3.hand.getValueh()) + """ | P4 TOTAL: """ + str(p4hand.getValueh()) + """ |
        ---------------------------------------------------------------------
        """)

#for convenience
def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


#THIS IS WHERE THE MAIN PROGRAM STARTS
dealerturn = False
playing = True
numplay = input("HELLO THERE, AND WELCOME TO BACKJACK! HOW MANY PLAYERS ARE YOU PLAYING WITH? (2,3,4)")
while numplay not in ["2","3","4"]:
    numplay = input("INVALID INPUT: PLEASE TRY AGAIN.(2,3,4)")

print("\nyou are playing with " + numplay + " players")
#Creating hand and chips class for each player
#every player has the same number of chips
input("""
RULES:
Win condition: person with the highest number less than or equal to 21 wins

In the beginning of each round, every player gets 2 cards, and so does the dealer, who covers one of their cards. The order 
of turns is as such:
 - P2
 - P3
 - P4
 - Dealer

During a turn, each player can choose to either "hit" or "stand", where a hit means take another card from the deck,
and a stand means to lock in their current cards. The three ways to end your turn are either to stand, hit exactly 21, 
or for the combined total of your cards to go above 21(you automatically lose). 

At the beginning of each round, a player can choose how many chips to bet, where the winner takes all the chips
at the end of the round, and ties split the prize pool evenly. If nobody wins, then all chips are lost. 

Aces can be either 11 or 1, and will be decided upon drawing your card, or at the beginning of your turn. Don't worry if it says
22 on the scorecard, that just means 2 aces.

(ENTER TO CONTINUE)
""")
try:
    total = int(input("\n\ntotal number of chips for each player(anything not a number will become 100)"))
except:
    total = 100

deck = Deck()
deck.reset()

p1chips = Chips(total,"Dealer")
p1hand = Hand("Dealer")
p1  = Player(p1hand,p1chips,"Dealer",True)

p2chips = Chips(total,"Player 2")
p2hand = Hand("Player 2")
p2 = Player(p2hand,p2chips,"Player 2",True)

if numplay in ["3","4"]:
    p3chips = Chips(total,"Player 3")
    p3hand = Hand("Player 3")
    p3 = Player(p3hand,p3chips,"Player 3",True)
else:
    p3 = Player(None,None,None,False)
    
if numplay == "4":
    p4chips = Chips(total,"Player 4")
    p4hand = Hand("Player 4")
else:
    p4 = Player(None,None,None,False)
    
#print(p1chips.getTotal()) test the beginning

    #gonna make a while loop here later
'''
p1hand.draw(Card("Spades","Two"))
p1hand.draw(Card("Spades","Ace"))
printUI(int(numplay))
'''
#play begins, and the first two cards are handed out

input("Every player gets 2 cards(enter to continue)")
clear()
hit(deck,p1.hand)
hit(deck,p1.hand)
p1.chips.make_bet()
hit(deck,p2.hand)
hit(deck,p2.hand)
p2.chips.make_bet()
total_bets = p1chips.getBet() + p2chips.getBet()
if int(numplay) >= 3:
    hit(deck,p3hand)
    hit(deck,p3hand)
    p3chips.make_bet()
    total_bets += p3chips.getBet()
if int(numplay) == 4:
    hit(deck,p4hand)
    hit(deck,p4hand)
    p4chips.make_bet()
    total_bets += p4chips.getBet()

printUI(int(numplay))
order = []
for x in range(2,int(numplay)+1):
    order.append("Player " + str(x))
order.append("Dealer")


#p2 plays
turn(p2)
#p3 plays
turn(p3)
#p4 plays
turn(p4)
#NOTE TO SELF: MAKE GODDAMN SURE YOU CHECK FOR ACES IN THE BEGINNING OF THE DEALER'S TURN
dealerturn = True
turn(p1)





"""
(Messae to self 11/23/20)
OKAY DONT PANIC. Your next step is to make sure you create a brand-new Player class. While creating this class, 
go back and fix a lot of the other Classes. Basically, this project aint going anywhere until you fix it all up.
FOR GODS SAKE PLEASE PLEASE PLEASE PUT ALL THE CLASSES IN A DIFFERENT FILE. This project is far from over, and, hey, better
now that in an actual work environment. Make sure its more organized in the code, and include more white space and clarity
using comments. Structure it in a way that makes sense and make sure everything is right this time before trying to continue.
You will grow from this, but you gotta push through the temporary dissapointment. Play some hype music, relax, and start
from the top.
"""