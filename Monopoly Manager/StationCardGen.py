# Purpose: File with functions for generating Station cards
from SpaceClasses import *
from PIL import Image, ImageDraw, ImageFont, ImageOps
import math

# Each of my Monopoly cards is 8 x 5.3 cm

# =====================================
def genStationCard(pStation, pStreetNameSize, pStreetNameStrokeW):

    mSymbol = "м"

    train = Image.open("cardPhotos/train.png", "r")

    cardHeight = cmToPix(8)
    cardWidth = cmToPix(5.3)

    standardTextSize = 30
    borderInset = 19

    multiplier = 3
    cardWidth = cardWidth * multiplier
    cardHeight = cardHeight * multiplier
    centre = (cardWidth / 2, cardHeight / 2)

    # Background
    card = Image.new("RGB", (cardWidth, cardHeight), color=(255, 255, 255))
    draw = ImageDraw.Draw(card)
    draw.rectangle(
        (borderInset, borderInset, cardWidth - borderInset, cardHeight - borderInset),
        fill=None,
        outline="black",
        width=3,
    )

    trainResizeFac = 5
    trainW, trainH = train.size
    trainW = trainW / trainResizeFac
    trainH = trainH / trainResizeFac

    train = train.resize((int(trainW), int(trainH)))
    card.paste(
        train,
        (int((cardWidth / 2) - (trainW / 2)), borderInset + 10),
        train,
    )

    myFont = ImageFont.truetype("arial.ttf", pStreetNameSize)
    text = pStation.getPropertyName().upper()
    w, h = draw.textsize(text, font=myFont)
    cenWidth = (cardWidth - w) / 2
    draw.text(
        (cenWidth, cmToPix(3.8) * multiplier),
        text,
        font=myFont,
        stroke_width=pStreetNameStrokeW,
        stroke_fill="black",
        fill="black",
    )

    myFont = ImageFont.truetype("arial.ttf", standardTextSize)

    for i in range(4):
        rentHeight = 450 + (64 * (i + 3)) - 32
        if i == 0:
            text = "RENT"
            draw.text(
                (borderInset + 10, rentHeight),
                text,
                anchor="lm",
                font=myFont,
                fill="black",
            )
        else:
            text = "If " + str(i + 1) + " Stations are owned"
            draw.text(
                (borderInset + 10, rentHeight),
                text,
                anchor="lm",
                font=myFont,
                fill="black",
            )

        text = mSymbol + str(pStation.getTrainStationRentList()[i])
        draw.text(
            (cardWidth - (borderInset + 10), rentHeight),
            text,
            anchor="rm",
            font=myFont,
            fill="black",
        )

    myFont = ImageFont.truetype("arial.ttf", 20)
    text = "© COPYRIGHT LOLOLOL"
    w, h = draw.textsize(text, font=myFont)
    cenWidth = (cardWidth - w) / 2
    draw.text(
        (cenWidth, cardHeight - (borderInset + 30)), text, font=myFont, fill="black"
    )

    card.save("savedPropertyCards/" + pStation.getPropertyName() + ".png")

    # card.show()


# =================


def cmToPix(pCM):
    return math.ceil(pCM * 37.7952755906)