# Purpose: To generate a player token

from PIL import Image, ImageDraw, ImageFont, ImageOps
import math

# Each of my Monopoly cards is 8 x 5.3 cm

# =====================================
def genPlayerToken(pIcon, pColour):

    resizeDict = {
        "battleship": 0.5,
        "tophat": 0.3,
        "cat": 0.5,
        "dog": 0.15,
        "penguin": 0.6,
        "duck": 0.65,
        "racecar": 0.6,
        "trex": 0.6,
    }

    playerIcon = Image.open("cardPhotos/" + pIcon + ".png", "r")

    tokenSize = cmToPix(8)
    cardHeight = cmToPix(8)
    cardWidth = cmToPix(5.3)

    standardTextSize = 30

    intTokenCentre = int(tokenSize / 8)
    centre = (intTokenCentre, intTokenCentre)

    # Background
    card = Image.new("RGBA", (tokenSize, tokenSize), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(card)

    # Draw a rounded rectangle

    draw.rounded_rectangle(
        (0, 0, tokenSize, tokenSize), fill=pColour, outline="black", width=3, radius=50
    )

    playerIconResizeFac = resizeDict[pIcon]
    playerIconW, playerIconH = playerIcon.size
    playerIconW = playerIconW * playerIconResizeFac
    playerIconH = playerIconH * playerIconResizeFac

    playerIcon = playerIcon.resize((int(playerIconW), int(playerIconH)))

    card.paste(
        playerIcon,
        (
            int((tokenSize / 2) - (playerIconW / 2)),
            int((tokenSize / 2) - (playerIconH / 2)),
        ),
        playerIcon,
    )

    card.save("playerTokens/" + pIcon + ".png")


# =================


def cmToPix(pCM):
    return math.ceil(pCM * 37.7952755906)
