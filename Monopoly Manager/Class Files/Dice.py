# Purpose: Customisable dice class

import math
import random
from itertools import *
from fractions import *


class Dice:
    def __init__(self, pNumOfFaces):
        self.numOfFaces = pNumOfFaces
        self.minNum = 1

    # Accessors ================================================================================================

    def getNumOfFaces(self):
        return self.numOfFaces

    def getMinNum(self):
        return self.minNum

    # Mutators ================================================================================================

    def setNumOfFaces(self, pNumOfFaces):
        self.numOfFaces = pNumOfFaces

    def setMinNum(self, pMinNum):
        self.minNum = pMinNum

    # Other ================================================================================================

    def rollDice(self):
        # Returns random number from minNum to numOfFaces (inclusive)
        return random.randint(self.minNum, self.numOfFaces)

    def copyObject(self):
        return Dice(self.getNumOfFaces())

    def equals(self, other):
        equal = False

        if isinstance(self, Dice) and isinstance(other, Dice):
            if vars(self) == vars(other):
                equal = True
        return equal

    def displayDice(self, pDisplayDictBool):
        for key in vars(self):
            print(f"{key} : {str((vars(self))[key])}")
        print()
        if pDisplayDictBool:
            print(self.__dict__)


"""
Function finds the probability of rolling a particular number with x amount of dice. 
"find" is the number you want to find the probability of.

E.g. getProb(4, 6, 8) finds the probability of getting 4 when rolling a 6-faced dice and an 8-faced dice which is 3/48
"""


def getProb(find, pValueList):

    rangeList = [range(1, i + 1) for i in pValueList]

    # print()
    # print(rangeList)
    # print(*rangeList)

    # diceComboList = list(product(range(1, 7), range(1, 7)))

    ## diceComboList is a list of tuples. Each tuple has as many numbers as there are dice
    diceComboList = list(product(*rangeList))

    print(
        "\nThe "
        + str(len(diceComboList))
        + " constructed dice Combinations : "
        + str(diceComboList)
    )

    ## for each tuple, add its elements and save the result as a new element in outcomes.

    ## Initialise the outcomes list.
    outcomes = []
    for tup in diceComboList:
        outcomes.append(sum(tup))

    # diceComboList = list(product("ABCD", repeat = 3))

    ## FIND ALL INSTANCES OF THE find NUMBER
    count = 0
    for i in outcomes:
        if i == find:
            count += 1

    sampleSpace = len(outcomes)

    """
    ## PRINTING RESULT

    print("\nOutcomes List:", str(outcomes))

    print(str(count), "/", str(sampleSpace))
    print(Fraction(count, sampleSpace))
    """

    return count / sampleSpace


'''
# =================================================================MAIN=================================================================


diceList = [Dice(6), Dice(8)]

for i in range(len(diceList)):
    print(f"Dice {i+1} Roll = {str(diceList[i].rollDice())}")

print(
    str(
        round(
            getProb(4, [diceList[0].getNumOfFaces(), diceList[1].getNumOfFaces()])
            * 100,
            4,
        )
    )
    + "%"
)
'''