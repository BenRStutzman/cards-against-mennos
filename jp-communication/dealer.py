import os, shutil

def deal(hand):
    for pic in os.scandir('hand'):
        os.remove(pic)
    for index, num in enumerate(hand):
        shutil.copy("cards\\black\\" + str(num) + ".png",
                    "static\\card" + str(index + 1) + ".png")

def test():
    deal([35, 3, 7, 19, 40, 8, 100])

if __name__ == '__main__':
    test()
