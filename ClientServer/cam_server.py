from server_module import *
import random 

# Please see README for how to add game logic to this program


## Pregame stuff 

## Server stuff
host = "10.6.28.148"
port = 1000
server = open_server(host, port)

## default constants
HANDSIZE = 7
NUMPLAYERS = 4
POINTSTOWIN = 2

## Set constants
#HANDSIZE = int(input("What handsize do you want to play with? (please be reasonable): "))
NUMPLAYERS = int(input("How many players want to play?: "))
#POINTSTOWIN = int(input("How many points do you need to win?: "))

print("Waiting for players...")
while len(server.players) < NUMPLAYERS: #wait till you have enough players
    pass

server.send_event('Welcome to Cards Against Mennonites!')


# Do stuff to make the game happen

## grab cards from text files
BlackCards = []
WhiteCards = []
f = open("BlackCards.txt", "r")
if f.mode == "r":
    BlackCards = f.read().split("\n")
f = open("WhiteCards.txt", "r")
if f.mode == "r":
    WhiteCards = f.read().split("\n")

## initialization
Players = []
DiscardBlackCards = []
DiscardWhiteCards = []
Done = False

## defining functions 
def DrawTopCard(deck, isBlack):
    if len(deck) == 0:
        if isBlack:
            deck += DiscardBlackCards
            DiscardBlackCards.clear()
        else:
            deck += DiscardWhiteCards
            DiscardWhiteCards.clear()
    randnum = random.randrange(0, len(deck), 1)
    card = deck.pop(randnum)
    DiscardBlackCards.append(card)
    return card

def DrawWhiteCards(hand):
    while len(hand) < HANDSIZE:
        card = DrawTopCard(WhiteCards, False)
        hand.append(card)
        DiscardWhiteCards.append(card)

## CAN ADD DIFFERENT GAME ENDING CONDITIONS
def CheckIfDone():
    ## simple for testing
##    inp = input("Do you want to continue playing? ('y'/'n'): ")
##    if inp == "y":
##        return False
##    elif inp == "n":
##        return True
##    else:
##        return CheckIfDone()

    ## points to win
    for i in range(len(Players)):
        if Players[i].Score >= POINTSTOWIN:
            print("\nPlayer ", i, " won!")
            return True
    return False

class Player:
    def __init__(self):
        self.Hand = []
        self.Score = 0
        self.BlackCardsWon = []

    def PlayWhiteCard(self, index):
        card = self.Hand.pop(index)
        return card

    def Mulligan(self):
        self.Hand = []
        DrawWhiteCards(self.Hand)


## create an array of Players and give them a starting hand
for i in range(NUMPLAYERS):
    NewPlayer = Player()
    Players.append(NewPlayer)
    DrawWhiteCards(Players[i].Hand)
    ## pass each Player's hand to server
    ## handy way to make a list a string found from https://www.decalage.info/en/python/print_list
    server.send_event("Your hand: " + str(Players[i].Hand).strip('[]'), player_ID = i)

    
    #print("Player ", i, "'s hand: ", Players[i].Hand)

# (See README for what server functions are available)


# just an example of getting responses
#server.send_event('What is your favorite letter?', time_lim = 10, num_chars = 1)
#responses = server.get_responses()
#for player, response in responses:
    #print("Player %s chose '%s'" % (player, response))


server.send_event("Thanks for playing!")
#server.close()
