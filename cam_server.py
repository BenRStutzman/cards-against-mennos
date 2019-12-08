from ClientServer.server_module import *
import random
import time

# Please see README for how to add game logic to this program

## Pregame stuff

## Server stuff
#host = "10.6.28.148" #Dan's Computer
host = '10.6.26.177' #Ben's Computer
#host = '10.6.28.230' #Isaac's Computer

port = 1000
server = open_server(host, port)

## default constants
HANDSIZE = 7
NUMPLAYERS = 4
POINTSTOWIN = 3
TIME_LIMIT = 30

## Set constants
#HANDSIZE = int(input("What handsize do you want to play with? (please be reasonable): "))
NUMPLAYERS = int(input("How many players want to play?: "))
#POINTSTOWIN = int(input("How many points do you need to win?: "))
#TIME_LIMIT = int(input("What do you want the time limit to be?: "))

print("Waiting for players...")
while len(server.players) < NUMPLAYERS: #wait to start game till you have enough players
    pass

server.send_event('Welcome to Cards Against Mennonites!')


# Do stuff to make the game happen

## grab cards from text files
BlackCards = []
WhiteCards = []
f = open("cards\\BlackCards.txt", "r")
if f.mode == "r":
    BlackCards = f.read().splitlines()
f = open("cards\\WhiteCards.txt", "r")
if f.mode == "r":
    WhiteCards = f.read().splitlines()
AllBlackCards = BlackCards.copy()
AllWhiteCards = WhiteCards.copy()
print(len(AllBlackCards))
print(len(AllWhiteCards))

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
    if isBlack:
        DiscardBlackCards.append(card)
    else:
        DiscardWhiteCards.append(card)
    return card

def DrawWhiteCards(hand):
    while len(hand) < HANDSIZE:
        card = DrawTopCard(WhiteCards, False)
        hand.append(card)

## CAN ADD DIFFERENT GAME ENDING CONDITIONS
def CheckIfDone():
    ## points to win
    for i in range(len(Players)):
        if Players[i].Score >= POINTSTOWIN:
            server.send_event("\n\nPlayer " + str(i) + " won!")
            server.send_event("\nYou won, congrats!", player_ID = i)
            #print("\nPlayer ", i, " won!")
            return True
    return False

def CardIDs(hand):
    return ' '.join([str(AllWhiteCards.index(card)) for card in hand])

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
        ## pass each Player their hand
        server.send_event("Here's your new hand.", details = CardIDs(Players[i].Hand), player_ID = i)

    ## initialize
    PlayedCards = []

    ## increment CardElderPosition
    CardElderPosition += 1
    if CardElderPosition > (NUMPLAYERS - 1):
        CardElderPosition = 0

    server.send_event("The judge for this round is player " + str(CardElderPosition) + '.', exclude = CardElderPosition)
    server.send_event("You are the judge for this round. Waiting for responses...", player_ID = CardElderPosition)

    ## draw a black card
    JudgesCard = DrawTopCard(BlackCards, True)
    ## check if black card is play 2
    IsPlayTwo = (-1 != JudgesCard.find("(pick 2)")) ## .find returns -1 if it does not find pick 2
    ## send everyone the black card
    server.send_event("Here's the judge's card.", details = str(AllBlackCards.index(JudgesCard)))

    ## retrieve the cards players want to play from all but the judge
    if IsPlayTwo:
        server.send_event('Which cards do you want to play? (indexing starts at 0; first index is first blank):', time_lim = TIME_LIMIT, num_chars = 2, exclude = CardElderPosition)
        PlayedCardsA = server.get_responses(num_needed = len(Players) - 1)
    else:
        server.send_event('Which card do you want to play?', time_lim = TIME_LIMIT, num_chars = 1, exclude = CardElderPosition)
        PlayedCardsA = server.get_responses(num_needed = len(Players) - 1)

    ## organize played cards data into a dict with submitted cards as keys that store the player that sent the card
    PlayedCardsB = {}
    for i in range(len(PlayedCardsA)):
        PlayerSubmitting = PlayedCardsA[i][0]
        if IsPlayTwo:
            positions = list(PlayedCardsA[i])[1]
            Card1 = Players[PlayerSubmitting].Hand[int(positions[0])]
            Card2 = Players[PlayerSubmitting].Hand[int(positions[1])]
            ## need to play the card with a greater index first so it doesn't mess up the index of the other card
            if positions[0] > positions[1]:
                Players[PlayerSubmitting].PlayWhiteCard(int(positions[0]))
                Players[PlayerSubmitting].PlayWhiteCard(int(positions[1]))
            else:
                Players[PlayerSubmitting].PlayWhiteCard(int(positions[1]))
                Players[PlayerSubmitting].PlayWhiteCard(int(positions[0]))
            PlayedCardsB[(Card1,Card2)] = PlayerSubmitting
        else:
            Card1 = Players[PlayerSubmitting].PlayWhiteCard(int(list(PlayedCardsA[i])[1]))
            PlayedCardsB[Card1] = PlayerSubmitting

    ## make a shuffled list of PlayedCards to give to judge
    keys =  list(PlayedCardsB.keys())
    random.shuffle(keys)

	## ask the judge to choose a winning card
    server.send_event("Here are the submissions.", details = CardIDs(keys))
    server.send_event("These are the submissions. Waiting for the judge to decide...", exclude = CardElderPosition)
    server.send_event("Which card wins?", time_lim = TIME_LIMIT, num_chars = 1, player_ID = CardElderPosition)
    WinningIndexRaw = server.get_responses(num_needed = 1)
    WinningIndex = WinningIndexRaw[0][1] ## WinningIndexRaw is an array of one tuple where the second index is the input from the judge
    WinningCard = keys[int(WinningIndex)]
    WinningPlayer = PlayedCardsB[WinningCard]

	## increment scores and tell players important information
    server.send_event("The judge chose player " + str(WinningPlayer) + "'s submission: " + str(WinningCard) + "!")
    ## increment winners score
    Players[WinningPlayer].Score += 1
    ## add BlackCard to that players pile of BlackCardsWon
    Players[WinningPlayer].BlackCardsWon.append(JudgesCard)
    tallyscores = "Current Scores: "
    scores = sorted([(i, Players[i].Score) for i in range(len(Players))], key = lambda x: x[1], reverse = True)
    for score in scores:
        tallyscores += "Player " + str(score[0]) + ": " + str(score[1]) + ", "
    server.send_event(tallyscores[:-2])
    Done = CheckIfDone()

## send player scores and BlackCardsWon
for i in range(NUMPLAYERS):
    server.send_event("\nYour score: " + str(Players[i].Score), player_ID = i)
    server.send_event("Black Cards Earned: " + str(Players[i].BlackCardsWon).strip('[]'), player_ID = i)


server.send_event("Thanks for playing!")
time.sleep(1) #makes sure there is time to complete other events
server.close()
