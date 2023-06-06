# Purpose: Class file to define Bank

class Bank:
    def __init__(
        self, pMoneyCache, pTotalMoneyGained, pTotalMoneyLost, pPropertiesOwned
    ):

        # Money can only be ADDED to the cache, only emptied with free parking
        # The bank has infinite money
        self.moneyCache = pMoneyCache
        self.totalMoneyGained = pTotalMoneyGained
        self.totalMoneyLost = pTotalMoneyLost
        self.propertiesOwned = pPropertiesOwned

    # Accessors ================================================================================================

    def getMoney(self):
        return self.moneyCache

    def getTotalMoneyGained(self):
        return self.totalMoneyGained

    def getTotalMoneyLost(self):
        return self.totalMoneyLost

    def getPropertiesOwned(self):
        return self.propertiesOwned

    # Mutators ================================================================================================

    def setMoney(self, pMoneyCache):
        self.moneyCache = pMoneyCache

    def setPropertiesOwned(self, pPropertiesOwned):
        self.propertiesOwned = pPropertiesOwned

    def setTotalMoneyGained(self, pTotalMoneyGained):
        self.totalMoneyGained = pTotalMoneyGained

    def setTotalMoneyLost(self, pTotalMoneyLost):
        self.totalMoneyLost = pTotalMoneyLost

    # ---------------------
    # These should really only be used inside the bank class
    def changeTotalMoneyGained(self, pTotalMoneyGained):
        self.totalMoneyGained += pTotalMoneyGained

    def changeTotalMoneyLost(self, pTotalMoneyLost):
        self.totalMoneyLost += pTotalMoneyLost

    # ---------------------
    # These should be used to add/take money from the bank
    def moneyToBank(self, pAddMoney):
        self.moneyCache += pAddMoney
        self.changeTotalMoneyGained(pAddMoney)

    def moneyFromBank(self, pTakeMoney):
        self.changeTotalMoneyLost(pTakeMoney)

    # Other ================================================================================================

    def copyObject(self):
        return Bank(
            self.getMoney(),
            self.getTotalMoneyGained(),
            self.getTotalMoneyLost(),
            self.getPropertiesOwned(),
        )

    def equals(self, other):
        equal = False

        if isinstance(self, Bank) and isinstance(other, Bank):
            if vars(self) == vars(other):
                equal = True
        return equal

    def displayBank(self, pDisplayDict):
        for key in vars(self):
            print(f"{key} : {str((vars(self))[key])}")
        print()
        if pDisplayDict:
            print(self.__dict__)
