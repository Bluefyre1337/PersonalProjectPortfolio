# Purpose: To generate the back of the property cards.

from SpaceClasses import *
from PIL import Image, ImageDraw, ImageFont, ImageOps
import math
import textwrap

# Each of my Monopoly cards is 8 x 5.3 cm

# =====================================
def genCardBack(pProperty, pPropertyNameSize, pPropertyNameStrokeW):

    mSymbol = "м"

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

    # Border
    draw.rectangle(
        (borderInset, borderInset, cardWidth - borderInset, cardHeight - borderInset),
        fill="red",
        outline=None,
        width=0,
    )

    # Print Property Name

    myFont = ImageFont.truetype("arial.ttf", pPropertyNameSize)
    text = pProperty.getPropertyName().upper()
    w, h = draw.textsize(text, font=myFont)

    while w > (cardWidth - (2 * borderInset)):
        pPropertyNameSize -= 1
        myFont = ImageFont.truetype("arial.ttf", pPropertyNameSize)
        w, h = draw.textsize(text, font=myFont)

    cenWidth = (cardWidth - w) / 2

    draw.text(
        (cenWidth, 100),
        text,
        font=myFont,
        stroke_width=pPropertyNameStrokeW,
        stroke_fill="white",
        fill="white",
    )

    myFont = ImageFont.truetype("arial.ttf", pPropertyNameSize)

    text = f"MORTAGE VALUE: {mSymbol}{pProperty.getMortgageValue()}"

    lines = textwrap.wrap(text, width=20)
    y_text = cardHeight / 2
    for line in lines:
        width, height = myFont.getsize(line)
        draw.text(
            (cardWidth / 2, y_text),
            line,
            anchor="mm",
            font=myFont,
            stroke_width=pPropertyNameStrokeW,
            stroke_fill="white",
            fill="white",
        )
        y_text += height

    text = f"TO UNMORTGAGE, PAY {mSymbol}{pProperty.getUnmortgageCost()}"

    lines = textwrap.wrap(text, width=20)
    y_text = y_text + 40
    for line in lines:
        width, height = myFont.getsize(line)
        draw.text(
            (cardWidth / 2, y_text),
            line,
            anchor="mm",
            font=myFont,
            stroke_width=pPropertyNameStrokeW,
            stroke_fill="white",
            fill="white",
        )
        y_text += height

    myFont = ImageFont.truetype("arial.ttf", 30)
    text = f"Card must be turned this side up if property is mortgaged."

    lines = textwrap.wrap(text, width=30)
    y_text = y_text + 200
    for line in lines:
        width, height = myFont.getsize(line)
        draw.text((cardWidth / 2, y_text), line, anchor="mm", font=myFont, fill="white")
        y_text += height

    card.save("savedPropertyCards/" + pProperty.getPropertyName() + " Back.png")

    # card.show()


# =================


def cmToPix(pCM):
    return math.ceil(pCM * 37.7952755906)
