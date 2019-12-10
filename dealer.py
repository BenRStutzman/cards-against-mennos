'''
functions used to "deal" cards into the players hand
by copying the correct card pictures into a folder (static)
from which the browser loads them
'''

import os, shutil, re

def deal(hand):
    # deal an entire hand of white cards, takes a list of card indices
    for pic in os.scandir('static'): #clear the folder of white cards
        if re.search("card\d",str(pic)):
            file_path = "static/" + re.search("(card.*?png)",str(pic))[0]
            os.remove(file_path)
    for index, num in enumerate(hand): #copy the new cards in
        shutil.copy("cards\\white\\" + num + ".png",
                    "static\\card" + str(index + 1) + ".png")
    for i in range(len(hand), 7): #fill the rest of the hand with blank cards
        shutil.copy("cards\\white\\-1.png",
                    "static\\card" + str(i + 1) + ".png")

def deal_black(ID):
    # deal the new black card into the folder
    for pic in os.scandir('static'): #clear the folder of black cards
        if re.search("black_card",str(pic)):
            file_path = "static/" + re.search("(black_card.png)",str(pic))[0]
            os.remove(file_path)
    shutil.copy("cards\\black\\" + ID + ".png", #copy it over
                "static\\black_card.png")

def test():
    deal([35, 3, 7, 19, 40, 8, 100])

if __name__ == '__main__':
    test()
