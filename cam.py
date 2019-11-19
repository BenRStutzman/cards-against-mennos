
import random
BlackCards = [ 'Favorite Advent traditions include _________________',
  'I can\'t be with someone who doesn\'t understand the importance of ___________',
  'When the family discussions get out of control and people start talking about________',
 'Yes, my belief in _________ is consistent with my belief in __________. (pick 2)',
  'Just because I\'m Mennonite, doesn\'t mean I have a ________',
  'Over the years, Mennonites have contributed a lot to __________.',
  'Mennonite mating rituals',
  'You keep using that term; I don\'t think you know what it means.',
  'What I find sexy ',
  'It\'s not true if it\'s not in _________.',
  'Nothing pleases me quite like a ______________ in a Sunday service.',
  'Which just goes to prove that Mennos are amazing entrepreneurs.',
  'Kids these days just don\'t understand about ___________',
  'I\'m not afraid of a zombie apocolypse because I\'ve already lived through ________________.',
  'Am I a bad Mennonite if I don\'t have any ________________?',
  'There\'s no such thing as ____________.',
   'Favorite vacation All is fair in ________ and ___________ (pick 2)',
  'What I\'m giving up for Lent:',
  'It\'s no use crying over _____________.',
  'My utopia includes _______________.',
  'All ________ is good',
  '_________ (pick 1)',
  '__________ is surely one of the signs of the apocolypse.',
  '_____________ is part of my faith exploration journey.',
  'The early bird gets the ______________',
  '__________ is just another way to say I love you.',
  'Why does no one today recognize the importance of  ____________?',
  'If a genie granted me one wish, I would abolish ______________.',
  'Be on the lookout for a new ______________.',
  'We\'ve got nothing to lose but our __________.',
  'Some are born to __________;  some aspire to _________ and  others have ___________ thrust  upon them (1 card)',
  '_________ is my hope of  salvation.',
  '___________: It\'s what real  mennonites do.',
  '_________ always gets me into  trouble.',
   '____________ makes me want  to _________. (pick 2)',
  'On earth as it is in Heaven just  means ____________.',
  'My Church taught me to feel  guilty about ___________.',
  'Beauty may be in the eye of the  beholder but ________ is  universally adored.',
   'Sure, there\'s no peace without  justice, but there\'s also no  __________ without  __________. (pick 2)',
  'Luke, use the ____________.',
  'A Little Bit of __________ is a  Dangerous Thing.',
  'The Enemy of My Enemy is My  Excuse for ______________.',
  'Toto, I\'ve a Feeling we\'re not in  ________ anymore.',
  'They may take our lives but  they\'ll never take our  __________.',
  'Friends don\'t let friends engage  in ___________.',
   'Will you let me be your _________? Pray that I will have the grace to let you be my _______ too. (pick 1)',
  'Do not let yourself be led into temptation by the ____________.',
  'If you haven\'t noticed ________, you\'re just not paying attention.',
  'All that Glitters is not ____________.',
  'All\'s Fair in Love and __________.',
  'As useful as _________ at a potluck.',
  'Death by a thousand __________.',
   'The rain falls on the _______ and the _________ alike. (pick 2)',
  'Out of the frying pan and into the __________.',
  'A good ________ is hard to find. The grass is always greener on the other side of the ________.',
  'One who lives by the _________ dies by the ___________.',
  'The Seven ________ of Highly Effective Mennonites',
  'The Life-Changing Magic of ____________.',
  'What to expect when you\'re ___________.',
  'A journey of a thousand miles begins with _________.',
  'One person\'s trash is another\'s __________.',
  'Sticks and stones may break my bones but ________ will never hurt me.',
  'The best things in life are ____________.',
  'Time flies when you\'re ___________.',
  'Truth is stranger than ___________.',
  'Be the ________ that you want to see in the world.',
  'Walk softly and carry a big ___________.',
  'My parents are_____________. You and I are related by __________.',
'  ',
  'I know you\'re a Mennonite by your ____________',
  'My religion doesn\'t allow this in my house',
  'When the going gets tough, the Mennonites start talking about _____________.',
  'Seeing this term makes me think there might be Mennonite terms I know nothing about.',
  'Now is the perfect time for ____________.',
  'All I really need to know I learned in ___________.',
   'They say the pen is mightier than the sword but I say the _________ is mightier than the _________. (pick 2)',
  'You can never have too many ______________.',
  'If you don\'t have anything nice to say, say it with (or while) __________.',
  'It\'s not over until ____________.',
  'Just please stop it already with all that talk about ___________.',
  'My pastor has convinced me of ____________.',
  'The Gospel writers weren\'t thinking of ________ when they wrote the Bible.',
  'I would never talk about _________ in front of a fellow Mennonite.',
  '___________ is where the power lies.',
  'We may not all be theologians but I know that ______ is True.',
  '__________ looks normal but it\'s not.',
  '__________ is the opiate of the masses.',
  'You won\'t believe what I learned about ___________.',
  'I\'m old enough to remember when ________ wasn\'t just a Mennonite thing.',
  'You had me at _________.',
  'Trust me - I\'m a _________.',
  'My Oma always told me that life is like a __________.',
  'A _________ a day keeps the deacon away.',
  'We\'re ignoring the ________ again .',
  'Good __________ make good neighbours.',
  'I\'ve never met a ________ I didn\'t like.',
  'Chicken Soup for the __________ Soul',
  '___________ are the devil\'s workshop.',
  'You\'re preaching to the __________.',
  'The only thing we have to fear is ____________.',
  '____________ matters today more than ever.',
  'Never feed the ____________.']

WhiteCards = [
 'Anabaptism',
  'Pitch Pipe',
  'Biblical Storytelling',
  'Discernment',
  'Spiritual Well-being',
  'Liturgical Dance',
  'Creation Care',
  'Modest Dress',
  'Mennonite Heritage',
  'Tours',
  'Zwiebach',
  'Being Fancy',
  'Sorrel',
  'Roll Kuchen',
  'Dressing Plain',
  'The Great Mennonite Identity Crisis',
  'Shoo Fly Pie',
  'GAMEO',
  'Mormons',
  'Potlucks',
  'The Mennonite Encyclopedia',
  'Electricity',
  'Colonies',
  'Oberholt\'s Whisky',
  'Confession of Faith',
  'Menno Simons',
  'Abomination',
  'Adult baptism',
  'More With Less',
  'Hymn Sing',
  'Nonviolence',
  'Mennonite-Girls-Can Cook',
  'The Radical Reformation',
  'Schmauntfat',
  'Der Bote',
  'Felix Manz',
  'Passive Aggressive tendencies',
  'The Martyrs\' Mirror',
  'Georg Blaurock',
  'Decision-making by Consensus',
  'Hymnology',
  'Neo-Anabaptism',
  'Dirk Willems',
  '#606',
  'Church unity',
  'Menno Lit',
  'The Servant Song',
  'The Log Cabin Quilt',
  'Separation from the World',
  'Mennonite Farmers Sausage',
  'Youth Events',
  'Schleitheim Confession',
  'Covenant',
  'A Prayer Chain',
  'Munster',
  'Forebearance',
  'The Social Gospel',
  'Humility',
  'Schism',
  'Peace and Social Justice Working Groups',
  'The Pink Menno Campaign',
  'Cape Dress',
  'Feeding the Hungry',
  'The Twig in Beaky Dove',
  'Bonnet',
  'welcoming congregations',
  'Fun',
  'Horse and Buggy',
  'Biblical Literalism',
  'Dancing',
  'Black bumpers',
  'Pursing the lips',
  'Pickles',
  'stewardship',
  'Unfathomable Secularism',
  'Autoharp',
  'Frugality',
  'Loaves and Fishes',
  'Conrad Grebel',
  'hard work',
  'Hospitality',
  'Summer camp',
  'Miriam Toews',
  'Refugee Sponsorship',
  'Assembling School Kits',
  'Paska',
  'Sharing the Good News',
  'Goshen',
  'fair trade jewellery',
  'Restorative justice',
  'Elkhart',
  'MCC',
  'A Redemptive Path',
  'The Daily Bonnet',
  'MC Canada',
  'Emerging Voices Initiative',
  'Sommerfelder',
  'MEDA',
  'Rethinking',
  'First Mennonite Church',
  'Rook',
  'Ushers',
  'Mennonite Your Way',
  'Dutch Blitz',
  'Pastoral Care',
  'The Bonnet Battles',
  'Winkler',
  'geneology',
  'Deaconesses',
  'Steinbach',
  'Peace and Conflict Studies',
  'Theological Diversity',
  'Lancaster County',
  'Worldly Behaviour',
  'The Conference formerly known as the General Conference',
  'Bluffton College ',
  'Old Colony ',
  'Old Mennonites',
  'Fresno ',
  'Quilting Bee ',
  'Old Order',
  'Kitchener-Waterloo ',
  'Volleyball Tournaments',
  'Amish',
  'Living More with Less',
  ' walk-a-mile ',
  ' Holdemann',
  'Community ',
  'Assembly ',
  'Patriarchy',
  'Russian Mennonites ',
  'Steinbach Church',
  'Elders',
  'Swiss ',
  'the Priesthood of All Believers',
  ' John Howard Yoder',
  'Plautdeutch ',
  'The Great Trek ',
  'Bergthal Mennonites',
  'Pennsylvania Dutch ',
  'Playing the Mennonite Game',
  'Conscientious Objectors',
  'Mexican Mennonites',
  ' World Conference ',
  ' Leamington',
  'The New Hymn Book',
  ' AMBS ',
  ' Hygiene Kits',
  'Sharing a Hymn Book ',
  'The Ban ',
  'Redemptive Violence',
  'Journeying Together',
  ' Church Discipline',
  '  War Taxes',
  'A Water Pistol ',
  'Sex while Standing ',
  'Barn Raisings',
  'Alcohol ',
  'Post-Modern Theology ',
  'Facebook',
  'Raffle Tickets ',
  'Peace Activism ',
  'Restorative Justice',
  'Bolivia ',
  'The Quiet in the Land ',
  'The Mission Field',
  'Peacemaking ',
  'Bible College ',
  'Eschatology',
  'Hymnody ',
  'Bible quizzing ',
  'Exegesis',
  'The Bulletin ',
  'Handel\'s Messiah ',
  'Platz',
  'Summer Sausage ',
  'Choir Practice ',
  'Faith Exploration Classes',
  'The Sunday School Picnic ',
  'Head Covering ',
  'Faspa',
  'True Evangelical Faith ',
  'Suspenders ',
  'Freiwilliges',
  'Fraktur ',
  'Sunflower Seeds',
  ' Migration ',
  ' Patterns',
  'The Benediction ',
  'Mennonite Hipsters ',
  'Public Confessions',
  'Germantown ',
  'The Relief Sale ',
  'Someone arguing that Mennonite is a religion not an ethnicity',
  'Anabaptist history ',
  'Thrift Stores ',
  'Mennonite Names',
  'Non-ethnic Mennonites ',
  'Mixed Marriages ',
  'Pig Butchering Parties',
  'Campfire Songs ',
  'Missions ',
  '4 part harmony',
  '1525 ',
  'The Salvation of Yash Siemens ',
  'Ministries',
  'Brandy ',
  'Mennonite-Made Furniture ',
  'Dogma',
  'Accountability ',
  'Sunday School ',
  'Daily Vacation Bible School',
  'Signing Petitions ',
  'Reconciliation ',
  'Structures of Power',
  'Positions of Privilege ',
  'Generosity ',
  'The Salt of the Earth',
  'Farming ',
  'Going on a Retreat ',
  'Faith Formation',
  'Rhubarb ',
  'Lay Leadership ',
  'Purity',
  'Rudy Wiebe ',
  'Communal Loneliness ',
  'Barbara Smucker',
  'Servant ',
  'Moral Leadership ',
  'Praise Songs',
  'Coffee Hour ',
  'Soup ',
  'Passing Judgement on Others',
  'Sprinking ',
  'Dunking ',
  'Pouring',
  'Child Evangelism',
  ' Late Adopters of Technology ',
  ' Auctions',
  'Mud Sales ',
  'Mennonite Brethren ',
  'Hypocrisy',
  'Evana Network ',
  'Freundschaft ',
  'Protestant Work Ethic',
  'Verenijke ',
  'The Elephant in the Room ',
  'Fences',
  'Justice',
  ' Happiness ',
  ' Tying Blankets',
  'Crokinole',
  'Claiming Other People\'s Heritage as Our Own',
  'Fellowship',
  'A Non-Practicing Ethnic Mennonite',
  'The Being a Faithful Church Process ',
  'Pacifism',
  'Foot Washing Services',
  ' The Great Commission',
  '  A Brood of Vipers',
  'Intentional Communities ',
  'Gardening',
  ' A Listening Group',
  'Working Groups ',
  'Vision ',
  'Task Forces',
  'The Lectionary ',
  'Grapes and Crackers for the Children',
  'Insisting on being identified as neither Catholic nor Protestant',
  'Consumer Boycotts ',
  'Memorizing Bible Verses',
  'The Johnnie Appleseed Song',
  'First Cousins Once Removed',
  'Small Group',
  'Gatherings',
  'Wondering whether Square Dancing counts as Dancing',
  'Geez Magazine',
  'The Canadian Mennonite Newsmagazine',
  'The Credit Union']

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


