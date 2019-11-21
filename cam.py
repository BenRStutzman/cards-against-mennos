
import random

## grab cards from text files
BlackCards = []
WhiteCards = []
f = open("BlackCards.txt", "r")
if f.mode == "r":
    BlackCards = f.read().split("\n")
f = open("WhiteCards.txt", "r")
if f.mode == "r":
    WhiteCards = f.read().split("\n")

## constants
HANDSIZE = 7
NUMPLAYERS = 4
POINTSTOWIN = 2

## initialization
Players = []
DiscardBlackCards = []
DiscardWhiteCards = []
Done = False

## defining functions for later use
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

## NOT DONE YET!!!!!!!!!!!!!!!!!
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
    
## Set constants
## get from server or something
HANDSIZE = int(input("What handsize do you want to play with? (please be reasonable): "))
NUMPLAYERS = int(input("How many players want to play?: "))
POINTSTOWIN = int(input("How many points do you need to win?: "))


## create an array of Players and give them a starting hand
for i in range(NUMPLAYERS):
    NewPlayer = Player()
    Players.append(NewPlayer)
    DrawWhiteCards(Players[i].Hand)
    ## pass each Player's hand to server
    print("Player ", i, "'s hand: ", Players[i].Hand)


## Play the game
CardElderPosition = NUMPLAYERS - 1
while not Done:
    ## everyone draw up to handsize
    for i in range(NUMPLAYERS):
        DrawWhiteCards(Players[i].Hand)
        ## pass each Player's new hand to server
        print("Player ", i, "'s hand: ", Players[i].Hand)
        
    ## initialize
    PlayedCards = []
    
    ## increment CardElderPosition
    CardElderPosition += 1
    #print("BUGTEST", CardElderPosition)
    if CardElderPosition > (NUMPLAYERS - 1):
        CardElderPosition = 0
    print("JUDGE FOR THIS ROUND IS: ", CardElderPosition)
    ## pass one BlackCard to server
    JudgesCard = DrawTopCard(BlackCards, True)
    ## check if black card is play 2
    IsPlayTwo = (-1 != JudgesCard.find("(pick 2)"))
    #print("IsPlayTwo?: ", IsPlayTwo)
    print("JUDGES CARD: ", JudgesCard)
    ## recieve an array of positions from server and play the cards at those positions
    ## while we don't have a server to do this
    for i in range(NUMPLAYERS):
        if i != CardElderPosition:
            print("PLAYER NUMBER ", i, "'s turn:")
            if IsPlayTwo:
                position = input("Which cards do you want to play? (give two indexes; ie: 2 3; first index is first blank): ")
                positions = position.split()
                print(positions)
                Card1 = Players[i].Hand[int(positions[0])]
                Card2 = Players[i].Hand[int(positions[1])]                                
                PlayedCards.append((Card1, Card2, i))
                if positions[0] > positions[1]:
                    Players[i].PlayWhiteCard(int(positions[0]))
                    Players[i].PlayWhiteCard(int(positions[1]))
                else:
                    Players[i].PlayWhiteCard(int(positions[1]))
                    Players[i].PlayWhiteCard(int(positions[0]))
            else:
                position = int(input("Which card do you want to play? (give an index): "))
                PlayedCards.append((Players[i].PlayWhiteCard(position), i))
            
    ## pass PlayedCards to server
    print(PlayedCards)
    ## receive which index of PlayedCards won
    WinningIndex = int(input("Which card won? (give an index: "))
    ## increment winners score
    Players[PlayedCards[WinningIndex][-1]].Score += 1
    ## add BlackCard to that players pile of BlackCardsWon
    Players[PlayedCards[WinningIndex][-1]].BlackCardsWon.append(JudgesCard)
    ## check if done playing
    Done = CheckIfDone()
    
        
## check player scores and BlackCardsWon
for i in range(NUMPLAYERS):
    print("Player ", i)
    print("Score: ", Players[i].Score)
    print("Black Cards Earned: ", Players[i].BlackCardsWon)


