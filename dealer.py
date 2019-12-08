import os, shutil

def deal(hand):
    for pic in os.scandir('static'):
        if pic.name.startswith("<DirEntry 'card"):
            os.remove(pic)
    for index, num in enumerate(hand):
        shutil.copy("cards\\white\\" + num + ".png",
                    "static\\card" + str(index + 1) + ".png")
    for i in range(len(hand), 7):
        shutil.copy("cards\\white\\-1.png",
                    "static\\card" + str(i + 1) + ".png")

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
