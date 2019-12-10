'''
Functions for creating the images of the cards.
Should only need to be used once, and again if card lists are changed.
'''

#PIL Code from code-maven.com

from PIL import Image, ImageDraw, ImageFont

def make_card(text, card_color, ID):
    letters_per_line = 18
    font_name = "arialbd"
    font_size = 28
    card_size = (300, 400)
    spacing = 35
    if card_color == 'black' and text[-1] not in ['.', '?', '!', ')', ':']:
        text += '.' #add a period if there isn't one.
    fnt = ImageFont.truetype('C:/Windows/Fonts/' + font_name + '.ttf', font_size)
    words = text.split()
    lines = []
    word = words[0]
    while word[0] == '_' and len(word) > 10:
        word = word[1:]
    line = word
    i = 0
    for word in words[1:]:
        while word[0] == '_' and len(word) > 10:
            word = word[1:]
        if len(word) > letters_per_line:
            print(word)
        if len(line) + len(word) + 1 <= letters_per_line:
            line += ' ' + word
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    #print(lines)
    if card_color == 'black':
        background_color = (0, 0, 0)
        text_color = (255, 255, 255)
    elif card_color == 'white':
        background_color = (255, 255, 255)
        text_color = (0, 0, 0)
    img = Image.new('RGB', card_size, color = background_color)

    d = ImageDraw.Draw(img)
    for index, line in enumerate(lines): #draw the text onto the image
        d.text((10, 10 + index * spacing), line, font = fnt, fill = text_color)

    img.save(card_color + '/' + str(ID) + ".png")

def make_blank_card(card_color, ID):
    # this makes a blank card, for displaying as a filler
    card_size = (300, 400)
    if card_color == 'black':
        background_color = (0, 0, 0)
        text_color = (255, 255, 255)
    elif card_color == 'white':
        background_color = (255, 255, 255)
        text_color = (0, 0, 0)

    img = Image.new('RGB', card_size, color = background_color)

    img.save(card_color + '/' + str(ID) + ".png")

if __name__ == '__main__':
    # if this python file is run directly, remake all the black and white cards
    f = open('BlackCards.txt')
    cards = f.read().splitlines()
    for index, card in enumerate(cards):
        make_card(card, 'black', index)
    f.close()

    f = open('WhiteCards.txt')
    cards = f.read().splitlines()
    for index, card in enumerate(cards):
        make_card(card, 'white', index)
    f.close()
