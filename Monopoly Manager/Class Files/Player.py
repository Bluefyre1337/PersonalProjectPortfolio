# Purpose: Class file to define Player

class Player:
    def __init__(
        self,
        pPlayerID,
        pName,
        pColour,
        pToken,
        pMoney,
        pTurnsInJail,
        pStreetsOwned,
        pColourGroupsOwned,
        pUtilitiesOwned,
        pTrainStationsOwned,
        pClaimedGo,
        pIsBankrupt,
        pInJail,
        pPosition,
    ):
        self.playerID = pPlayerID
        self.name = pName
        self.colour = pColour
        self.token = pToken
        self.money = pMoney
        self.turnsInJail = pTurnsInJail
        self.streetsOwned = pStreetsOwned
        self.colourGroupsOwned = pColourGroupsOwned
        self.utilitiesOwned = pUtilitiesOwned
        self.trainStationsOwned = pTrainStationsOwned
        self.claimedGo = pClaimedGo
        self.isBankrupt = pIsBankrupt
        self.inJail = pInJail
        self.position = pPosition

    # Accessors ================================================================================================

    def getPlayerID(self):
        return self.playerID

    def getName(self):
        return self.name

    def getColour(self):
        return self.colour

    def getToken(self):
        return self.token

    def getMoney(self):
        return self.money

    def getTurnsInJail(self):
        return self.turnsInJail

    def getStreetsOwned(self):
        return self.streetsOwned

    def getColourGroupsOwned(self):
        return self.colourGroupsOwned

    def getUtilitiesOwned(self):
        return self.utilitiesOwned

    def getTrainStationsOwned(self):
        return self.trainStationsOwned

    def getClaimedGo(self):
        return self.claimedGo

    def getIsBankrupt(self):
        return self.isBankrupt

    def getInJail(self):
        return self.inJail

    def getPosition(self):
        return self.position

    def getPropertiesOwned(self):
        propertyOwnedList = []
        for street in self.streetsOwned:
            propertyOwnedList.append(street)
        for trainStation in self.trainStationsOwned:
            propertyOwnedList.append(trainStation)
        for utility in self.utilitiesOwned:
            propertyOwnedList.append(utility)
        return propertyOwnedList

    # Mutators ================================================================================================

    def setPlayerID(self, pPlayerID):
        self.playerID = pPlayerID

    def setName(self, pName):
        self.name = pName

    def setColour(self, pColour):
        self.colour = pColour

    def setToken(self, pToken):
        self.token = pToken

    def setMoney(self, pMoney):
        self.money = pMoney

    def changeMoney(self, pChange):
        self.money += pChange

    def setTurnsInJail(self, pTurnsInJail):
        self.turnsInJail = pTurnsInJail

    def setStreetsOwned(self, pStreetsOwned):
        self.streetsOwned = pStreetsOwned

    def setColourGroupsOwned(self, pColourGroupsOwned):
        self.colourGroupsOwned = pColourGroupsOwned

    def setUtilitiesOwned(self, pUtilitiesOwned):
        self.utilitiesOwned = pUtilitiesOwned

    def setTrainStationsOwned(self, pTrainStationsOwned):
        self.trainStationsOwned = pTrainStationsOwned

    def addStreet(self, pStreet):
        self.streetsOwned.append(pStreet)

    def addTrainStation(self, pTrainStation):
        self.trainStationsOwned.append(pTrainStation)

    def addUtility(self, pUtility):
        self.utilitiesOwned.append(pUtility)

    def setClaimedGo(self, pClaimedGo):
        self.claimedGo = pClaimedGo

    def setIsBankrupt(self, pIsBankrupt):
        self.isBankrupt = pIsBankrupt

    def setInJail(self, pInJail):
        self.inJail = pInJail

    def setPosition(self, pPosition):
        self.position = pPosition

    # Other ================================================================================================

    def doIOwn(self, pProperty):
        propertyOwned = False

        propertiesOwnedList = self.getPropertiesOwned()
        for property in propertiesOwnedList:
            propertyOwned = pProperty.equals(property)
        
        return propertyOwned

    def copyObject(self):
        return Player(
            self.getPlayerID(),
            self.getName(),
            self.getColour(),
            self.getToken(),
            self.getMoney(),
            self.getTurnsInJail(),
            self.getPropertiesOwned(),
            self.getColourGroupsOwned(),
            self.getUtilitiesOwned(),
            self.getTrainStationsOwned(),
            self.getClaimedGo(),
            self.getIsBankrupt(),
            self.getInJail(),
            self.getPosition(),
        )

    """
    def copyObject2(self):
        newObj = Player()
        for key in vars(self):
            setattr(newObj, key, vars(self)[key])
        return newObj
    """

    # put instance variables into dictionary or array/list to shorten .equals()?
    # https://stackoverflow.com/questions/6423814/is-there-a-way-to-check-if-two-object-contain-the-same-values-in-each-of-their-v

    """
    Using this method to compare dictionaries that correspond to the compared objects is probably better than individually iterating through each attribute.
    If you had two objects of different classes that both inherited from the same parent class, they would both be instances of that parent class.
    But they are not the same.
    Checking using this method (calling on the parent class) means that even though they pass the "isInstance" test, if they have different parameters of their own, they will fail the second check, and appear as different objects.
    Of course, this situation wouldn't occur in the first place because you always call the .equals on one of the objects to compare.
    """

    def equals(self, other):
        equal = False

        """
        print(vars(self))
        print(vars(other))
        print(vars(self) == vars(other))
        print(type(self))
        print(type(other))
        print(
            f"Both Player object?: {isinstance(self, Player) and isinstance(other, Player)}"
        )
        """

        if isinstance(self, Player) and isinstance(other, Player):
            if vars(self) == vars(other):
                equal = True
        return equal

    def displayPlayer(self, pDisplayDictBool):
        for key in vars(self):
            print(f"{key} : {str((vars(self))[key])}")
        print()
        if pDisplayDictBool:
            print(self.__dict__)


