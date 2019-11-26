from server_module import *
import random 

# Please see README for how to add game logic to this program


## Pregame stuff 

## Server stuff
host = "10.6.28.230"
port = 1000
server = open_server(host, port)

## default constants
HANDSIZE = 7
NUMPLAYERS = 4
POINTSTOWIN = 2
TIME_LIMIT = 20

## Set constants
#HANDSIZE = int(input("What handsize do you want to play with? (please be reasonable): "))
NUMPLAYERS = int(input("How many players want to play?: "))
#POINTSTOWIN = int(input("How many points do you need to win?: "))
#TIME_LIMIT = int(input("What do you want the time limit to be?: "))

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
            server.send_event("Player " + str(i) + " won!")
            #print("\nPlayer ", i, " won!")
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
    ##server.send_event("Your hand: " + str(Players[i].Hand).strip('[]'), player_ID = i)

# Play the game
CardElderPosition = NUMPLAYERS - 1
while not Done:
    ## everyone draw up to handsize
    for i in range(NUMPLAYERS):
        DrawWhiteCards(Players[i].Hand)
        ## pass each Player's new hand to server
        server.send_event("Your hand: " + str(Players[i].Hand).strip('[]'), player_ID = i)
        
    ## initialize
    PlayedCards = []
    
    ## increment CardElderPosition
    CardElderPosition += 1
    #print("BUGTEST", CardElderPosition)
    if CardElderPosition > (NUMPLAYERS - 1):
        CardElderPosition = 0
    server.send_event("JUDGE FOR THIS ROUND IS: " + str(CardElderPosition))
    ## pass one BlackCard to server
    JudgesCard = DrawTopCard(BlackCards, True)
    ## check if black card is play 2
    IsPlayTwo = (-1 != JudgesCard.find("(pick 2)"))
    #print("IsPlayTwo?: ", IsPlayTwo)
    server.send_event("JUDGES CARD: " + str(JudgesCard))
    ## recieve an array of positions from server and play the cards at those positions
    ## while we don't have a server to do this
##server.event


    if IsPlayTwo:
        server.send_event('Which cards do you want to play? (first index is first blank):', time_lim = TIME_LIMIT, num_chars = 3, exclude = CardElderPosition)
        PlayedCardsA = server.get_responses(num_needed = len(Players) - 1)
    else:
        server.send_event('Which cards do you want to play? (give one index):', time_lim = TIME_LIMIT, num_chars = 1, exclude = CardElderPosition)
        PlayedCardsA = server.get_responses(num_needed = len(Players) - 1)

    print(PlayedCardsA)
    PlayedCardsB = []
    for i in range(len(PlayedCardsA)):
        if IsPlayTwo:
            positions = list(PlayedCardsA[i])[1].split()
            Card1 = Players[i].Hand[int(positions[0])]
            Card2 = Players[i].Hand[int(positions[1])]                                
            PlayedCardsB.append((Card1,Card2,i))
        else:
            PlayedCardsB.append((Players[i].Hand[int(list(PlayedCardsA[i])[1])],i))


##    for i in range(NUMPLAYERS):
##        if i != CardElderPosition:
##            print("PLAYER NUMBER ", i, "'s turn:")
##            if IsPlayTwo:
##                position = input("Which cards do you want to play? (give two indexes; ie: 2 3; first index is first blank): ")
##
##
##                positions = position.split()
##                print(positions)
##                Card1 = Players[i].Hand[int(positions[0])]
##                Card2 = Players[i].Hand[int(positions[1])]                                
##                PlayedCards.append((Card1, Card2, i))
##                if positions[0] > positions[1]:
##                    Players[i].PlayWhiteCard(int(positions[0]))
##                    Players[i].PlayWhiteCard(int(positions[1]))
##                else:
##                    Players[i].PlayWhiteCard(int(positions[1]))
##                    Players[i].PlayWhiteCard(int(positions[0]))
##            else:
##                position = int(input("Which card do you want to play? (give an index): "))
##                PlayedCards.append((Players[i].PlayWhiteCard(position), i))
##            
    ## pass PlayedCards to server
    ## make a shuffled list of PlayedCards to give to judge
    toJudge = random.shuffle(PlayedCardsB)
    print(toJudge)
    for thing in toJudge:
        thing = list(thing).remove(-1)
    server.send_event("Here are your choices (give the index of the winning card): " + str(toJudge).strip('[]'), time_lim = TIME_LIMIT, num_chars = 1, player_ID = CardElderPosition)
    WinningIndex = server.get_responses(num_needed = 1)
    WinningCard = toJudge[WinningIndex]
    WinningPlayer = list(PlayededCardsB[PlayedCardsB.index(WinningCard)])[-1]
    server.send_event("Player " + str(WinningPlayer) + "'s card: " + WinningCard + " won!")
    ## increment winners score
    Players[WinningPlayer].Score += 1
    ## add BlackCard to that players pile of BlackCardsWon
    Players[WinningPlayer].BlackCardsWon.append(JudgesCard)
    ## check if done playing
    Done = CheckIfDone()
    
        
## check player scores and BlackCardsWon
for i in range(NUMPLAYERS):
    server.send_event("Your score: " + str(Players[i].Score), player_ID = i)
    server.send_event("Black Cards Earned: " + str(Players[i].BlackCardsWon).strip('[]'), player_ID = i)






    
    #print("Player ", i, "'s hand: ", Players[i].Hand)

# (See README for what server functions are available)


# just an example of getting responses
#server.send_event('What is your favorite letter?', time_lim = 10, num_chars = 1, exclude = )
#responses = server.get_responses()
#for player, response in responses:
    #print("Player %s chose '%s'" % (player, response))


server.send_event("Thanks for playing!")
#server.close()
