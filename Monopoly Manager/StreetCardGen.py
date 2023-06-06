# Purpose: File with functions for generating Street cards
from SpaceClasses import *
from PIL import Image, ImageDraw, ImageFont, ImageOps
import math

# Each of my Monopoly cards is 8 x 5.3 cm

# =====================================
def genStreetCard(pStreet, pColour, pTDCol, pStreetNameSize, pStreetNameStrokeW):

    mSymbol = "м"

    house1 = Image.open("cardPhotos/house1.png", "r")
    house2 = Image.open("cardPhotos/house2.png", "r")
    house3 = Image.open("cardPhotos/house3.png", "r")
    house4 = Image.open("cardPhotos/house4.png", "r")
    hotel = Image.open("cardPhotos/hotel.png", "r")
    buildingList = [house1, house2, house3, house4, hotel]

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

    # Draw Coloured rectangle
    colourBottom = cmToPix(1.8) * multiplier
    draw.rectangle(
        (borderInset, borderInset, cardWidth - borderInset, colourBottom),
        fill=pColour,
        width=0,
    )

    # Border
    draw.rectangle(
        (borderInset, borderInset, cardWidth - borderInset, cardHeight - borderInset),
        fill=None,
        outline="black",
        width=3,
    )

    draw.line(
        (borderInset, colourBottom, cardWidth - borderInset, colourBottom),
        fill="black",
        width=2,
    )

    # Draw divider line
    dividerWidthCut = 20
    dividerHeight = cmToPix(5.8) * multiplier
    draw.line(
        (
            borderInset + dividerWidthCut,
            dividerHeight,
            (cardWidth - borderInset) - dividerWidthCut,
            dividerHeight,
        ),
        fill="black",
        width=2,
    )

    # Print Title Deed
    myFont = ImageFont.truetype("arial.ttf", 20)
    text = "TITLE DEED"
    w, h = draw.textsize(text, font=myFont)
    cenWidth = (cardWidth - w) / 2
    draw.text((cenWidth, 40), text, font=myFont, fill=pTDCol)

    # Print Property Name
    myFont = ImageFont.truetype("arial.ttf", pStreetNameSize)
    text = pStreet.getPropertyName().upper()
    w, h = draw.textsize(text, font=myFont)

    while w > (cardWidth - (2 * borderInset)):
        pStreetNameSize -= 1
        myFont = ImageFont.truetype("arial.ttf", pStreetNameSize)
        w, h = draw.textsize(text, font=myFont)

    cenWidth = (cardWidth - w) / 2

    draw.text(
        (cenWidth, 100),
        text,
        font=myFont,
        stroke_width=pStreetNameStrokeW,
        stroke_fill="white",
        fill="black",
    )

    myFont = ImageFont.truetype("arial.ttf", standardTextSize)
    text = "Rent"
    draw.text(
        (borderInset + 10, (colourBottom + 32)),
        text,
        anchor="lm",
        font=myFont,
        fill="black",
    )

    text = "Rent with colour set"
    draw.text(
        (borderInset + 10, (colourBottom + 96)),
        text,
        anchor="lm",
        font=myFont,
        fill="black",
    )

    for i in range(5):
        text = "Rent with "
        draw.text(
            (borderInset + 10, (colourBottom + (64 * (i + 3)) - 32)),
            text,
            anchor="lm",
            font=myFont,
            fill="black",
        )

        curHouse = buildingList[i]
        curHouse = curHouse.resize((int(715 / 12), int(593 / 12)))
        card.paste(curHouse, ((160, (colourBottom + (64 * (i + 3)) - 60))), curHouse)

    for i in range(7):
        if i == 0:
            text = mSymbol + str(pStreet.getDefaultRent())
        elif i == 1:
            text = mSymbol + str(pStreet.getDefaultRent() * 2)
        elif i == 6:
            text = mSymbol + str(pStreet.getHotelRentItem(0))
        else:
            text = mSymbol + str(pStreet.getHouseRentItem(i - 2))

        draw.text(
            (cardWidth - (borderInset + 10), (colourBottom + (64 * (i + 1)) - 32)),
            text,
            anchor="rm",
            font=myFont,
            fill="black",
        )

    # HOUSE COSTS======================
    text = "Houses cost"
    draw.text(
        (borderInset + 10, (dividerHeight + 32)),
        text,
        anchor="lm",
        font=myFont,
        fill="black",
    )
    text = mSymbol + str(pStreet.getHouseCost()) + " each"

    draw.text(
        (cardWidth - (borderInset + 10), (dividerHeight + 32)),
        text,
        anchor="rm",
        font=myFont,
        fill="black",
    )

    # HOTEL COSTS======================
    text = "Hotels cost"
    draw.text(
        (borderInset + 10, (dividerHeight + 96)),
        text,
        anchor="lm",
        font=myFont,
        fill="black",
    )

    text = mSymbol + str(pStreet.getHotelCost()) + " each"

    draw.text(
        (cardWidth - (borderInset + 10), (dividerHeight + 96)),
        text,
        anchor="rm",
        font=myFont,
        fill="black",
    )

    myFont = ImageFont.truetype("arial.ttf", 20)
    text = "(plus 4 houses)"

    draw.text(
        (cardWidth - (borderInset + 10), (dividerHeight + 128)),
        text,
        anchor="rm",
        font=myFont,
        fill="black",
    )
    # ----------------------

    myFont = ImageFont.truetype("arial.ttf", 20)
    text = "© COPYRIGHT LOLOLOL"
    w, h = draw.textsize(text, font=myFont)
    cenWidth = (cardWidth - w) / 2
    draw.text(
        (cenWidth, cardHeight - (borderInset + 30)), text, font=myFont, fill="black"
    )

    card.save("savedPropertyCards/" + pStreet.getPropertyName() + ".png")

    # card.show()


# =================


def cmToPix(pCM):
    return math.ceil(pCM * 37.7952755906)
