import os, shutil, re

def deal(hand):
    for pic in os.scandir('static'):
        if re.search("card\d",str(pic)):
            file_path = "static/" + re.search("(card.*?png)",str(pic))[0]
            os.remove(file_path)
    for index, num in enumerate(hand):
        shutil.copy("cards\\white\\" + num + ".png",
                    "static\\card" + str(index + 1) + ".png")
    for i in range(len(hand), 7):
        shutil.copy("cards\\white\\-1.png",
                    "static\\card" + str(i + 1) + "_blank.png")

def deal_black(ID):
    for pic in os.scandir('static'):
        if pic.name == "<DirEntry 'black_card.png'>":
            os.remove(pic)
    shutil.copy("cards\\black\\" + ID + ".png",
                "static\\black_card.png")

def test():
    deal([35, 3, 7, 19, 40, 8, 100])

if __name__ == '__main__':
    test()
