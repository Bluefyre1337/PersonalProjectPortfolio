# Purpose: File with functions for generating Utility cards
from SpaceClasses import *
from PIL import Image, ImageDraw, ImageFont, ImageOps
import math
import textwrap

# Each of my Monopoly cards is 8 x 5.3 cm

# =====================================
def genUtilityCard(pUtility, pUtilityNameSize, pUtilityNameStrokeW, pIconFileName):

    utility = Image.open("cardPhotos/" + pIconFileName, "r")

    cardHeight = cmToPix(8)
    cardWidth = cmToPix(5.3)

    standardTextSize = 30
    borderInset = 19
    multiplier = 3

    cardWidth = cardWidth * multiplier
    cardHeight = cardHeight * multiplier

    centre = (cardWidth / 2, cardHeight / 2)

    utilityResizeFac = 0.5
    utilityW, utilityH = utility.size
    utilityW = utilityW * utilityResizeFac
    utilityH = utilityH * utilityResizeFac

    # Background
    card = Image.new("RGB", (cardWidth, cardHeight), color=(255, 255, 255))
    draw = ImageDraw.Draw(card)
    draw.rectangle(
        (borderInset, borderInset, cardWidth - borderInset, cardHeight - borderInset),
        fill=None,
        outline="black",
        width=3,
    )

    utility = utility.resize((int(utilityW), int(utilityH)))
    card.paste(
        utility,
        (int((cardWidth / 2) - (utilityW / 2)), borderInset + 10),
        utility,
    )

    myFont = ImageFont.truetype("arial.ttf", pUtilityNameSize)
    text = pUtility.getPropertyName().upper()
    w, h = draw.textsize(text, font=myFont)
    cenWidth = (cardWidth - w) / 2
    draw.text(
        (cenWidth, cmToPix(3.5) * multiplier),
        text,
        font=myFont,
        stroke_width=pUtilityNameStrokeW,
        stroke_fill="black",
        fill="black",
    )

    myFont = ImageFont.truetype("arial.ttf", standardTextSize)

    text = f"If one Utility is owned, rent is {pUtility.getDiceMultiplierItem(0)} times amount shown on dice."

    lines = textwrap.wrap(text, width=30)
    y_text = (cardHeight / 2) + 40
    for line in lines:
        width, height = myFont.getsize(line)
        draw.text((cardWidth / 2, y_text), line, anchor="mm", font=myFont, fill="black")
        y_text += height

    text = f"If both Utilities are owned, rent is {pUtility.getDiceMultiplierItem(1)} times amount shown on dice."

    lines = textwrap.wrap(text, width=30)
    y_text = y_text + 40
    for line in lines:
        width, height = myFont.getsize(line)
        draw.text((cardWidth / 2, y_text), line, anchor="mm", font=myFont, fill="black")
        y_text += height

    myFont = ImageFont.truetype("arial.ttf", 20)
    text = "© COPYRIGHT LOLOLOL"
    w, h = draw.textsize(text, font=myFont)
    cenWidth = (cardWidth - w) / 2
    draw.text(
        (cenWidth, cardHeight - (borderInset + 30)), text, font=myFont, fill="black"
    )

    card.save("savedPropertyCards/" + pUtility.getPropertyName() + ".png")

    # card.show()


# =================


def cmToPix(pCM):
    return math.ceil(pCM * 37.7952755906)