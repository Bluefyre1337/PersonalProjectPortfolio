# Purpose: Class file to define Spaces


class Space:
    def __init__(self, pSpaceID):
        self.spaceID = pSpaceID

    # Accessors ================================================================================================

    def getSpaceID(self):
        return self.spaceID

    # Mutators ================================================================================================

    def setSpaceID(self, pSpaceID):
        self.spaceID = pSpaceID

    # Other ================================================================================================

    def copyObject(self):
        return Space(self.getSpaceID())

    def equals(self, other):
        equal = False

        if isinstance(self, Space) and isinstance(other, Space):
            if vars(self) == vars(other):
                equal = True
        return equal

    def displaySpace(self, pDisplayDictBool):
        for key in vars(self):
            print(f"{key} : {str((vars(self))[key])}")
        print()
        if pDisplayDictBool:
            print(self.__dict__)


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class Property(Space):
    def __init__(
        self, pSpaceID, pPropertyName, pPropertyCost, pMortgageValue, pUnmortgageCost, pOwned
    ):
        super().__init__(pSpaceID)
        self.propertyName = pPropertyName
        self.propertyCost = pPropertyCost
        self.mortgageValue = pMortgageValue
        self.unmortgageCost = pUnmortgageCost
        self.owned = pOwned

    # Accessors ================================================================================================

    def getPropertyName(self):
        return self.propertyName

    def getPropertyCost(self):
        return self.propertyCost

    def getMortgageValue(self):
        return self.mortgageValue

    def getUnmortgageCost(self):
        return self.unmortgageCost

    def getOwned(self):
        return self.owned

    # Mutators ================================================================================================

    def setPropertyName(self, pPropertyName):
        self.propertyName = pPropertyName

    def setPropertyCost(self, pPropertyCost):
        self.propertyCost = pPropertyCost

    def setMortgageValue(self, pMortgageValue):
        self.mortgageValue = pMortgageValue

    def setUnmortgageCost(self, pUnmortgageCost):
        self.unmortgageCost = pUnmortgageCost

    def setOwned(self, pOwned):
        self.owned = pOwned

    # Other ================================================================================================

    def copyObject(self):
        return Property(
            self.getSpaceID(),
            self.getPropertyName(),
            self.getPropertyCost(),
            self.getMortgageValue(),
            self.getUnmortgageCost(),
            self.getOwned()
        )

    def equals(self, other):
        equal = False

        if isinstance(self, Property) and isinstance(other, Property):
            if vars(self) == vars(other):
                equal = True
        return equal


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class Street(Property):
    def __init__(
        self,
        pSpaceID,
        pPropertyName,
        pPropertyCost,
        pMortgageValue,
        pUnmortgageCost,
        pOwned,
        pStreetColour,
        pDefaultRent,
        pColourSetRent,
        pHouseRentList,
        pHotelRentList,
        pHouseCost,
        pHotelCost,
    ):
        super().__init__(
            pSpaceID, pPropertyName, pPropertyCost, pMortgageValue, pUnmortgageCost, pOwned
        )
        self.streetColour = pStreetColour
        self.defaultRent = pDefaultRent
        self.colourSetRent = pColourSetRent
        self.houseRentList = pHouseRentList
        self.hotelRentList = pHotelRentList
        self.houseCost = pHouseCost
        self.hotelCost = pHotelCost

    # Accessors ================================================================================================

    def getStreetColour(self):
        return self.streetColour

    def getDefaultRent(self):
        return self.defaultRent

    def getColourSetRent(self):
        return self.colourSetRent

    def getHouseRentList(self):
        return self.houseRentList

    def getHotelRentList(self):
        return self.hotelRentList

    # Allows you to select which house rent you want
    def getHouseRentItem(self, pIndex):
        return (self.houseRentList)[pIndex]

    # Allows you to select which hotel rent you want
    def getHotelRentItem(self, pIndex):
        return (self.hotelRentList)[pIndex]

    def getHouseCost(self):
        return self.houseCost

    def getHotelCost(self):
        return self.hotelCost

    # Mutators ================================================================================================

    def setStreetColour(self, pStreetColour):
        self.streetColour = pStreetColour

    def setDefaultRent(self, pDefaultRent):
        self.defaultRent = pDefaultRent

    def setColourSetRent(self, pColourSetRent):
        self.colourSetRent = pColourSetRent

    def setHouseRentList(self, pHouseRentList):
        self.houseRentList = pHouseRentList

    def setHotelRentList(self, pHotelRentList):
        self.hotelRentList = pHotelRentList

    # Allows you to change the house rent you want
    def setHouseRentItem(self, pIndex, pNewHouseRent):
        (self.houseRentList)[pIndex] = pNewHouseRent

    # Allows you to change the hotel rent you want
    def setHotelRentItem(self, pIndex, pNewHotelRent):
        (self.hotelRentList)[pIndex] = pNewHotelRent

    def setHouseCost(self, pHouseCost):
        self.houseCost = pHouseCost

    def setHotelCost(self, pHotelCost):
        self.hotelCost = pHotelCost

    # Other ================================================================================================

    def copyObject(self):
        return Street(
            self.getSpaceID(),
            self.getPropertyName(),
            self.getPropertyCost(),
            self.getMortgageValue(),
            self.getUnmortgageCost(),
            self.getStreetColour(),
            self.getDefaultRent(),
            self.getColourSetRent(),
            self.getHouseRentList(),
            self.getHotelRentList(),
            self.getHouseCost(),
            self.getHotelCost(),
        )

    def equals(self, other):
        equal = False

        if isinstance(self, Street) and isinstance(other, Street):
            if vars(self) == vars(other):
                equal = True
        return equal


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class Utility(Property):
    def __init__(
        self,
        pSpaceID,
        pPropertyName,
        pPropertyCost,
        pMortgageValue,
        pUnmortgageCost,
        pOwned,
        pDiceMultiplierList,
    ):
        super().__init__(
            pSpaceID, pPropertyName, pPropertyCost, pMortgageValue, pUnmortgageCost, pOwned
        )
        self.diceMultiplierList = pDiceMultiplierList
        # E.g. Element 0 is with 1 utility

    # Accessors ================================================================================================

    def getDiceMultiplierList(self):
        return self.diceMultiplierList

    # Allows you to select which multiplier you want
    def getDiceMultiplierItem(self, pIndex):
        return (self.diceMultiplierList)[pIndex]

    # Mutators ================================================================================================

    def setDiceMultiplierList(self, pDiceMultiplierList):
        self.diceMultiplierList = pDiceMultiplierList

    # Allows you to change the multiplier you want
    def setDiceMultiplierItem(self, pIndex, pNewDiceMultiplier):
        (self.diceMultiplierList)[pIndex] = pNewDiceMultiplier

    # Other ================================================================================================

    def copyObject(self):
        return Utility(
            self.getSpaceID(),
            self.getPropertyName(),
            self.getPropertyCost(),
            self.getMortgageValue(),
            self.getUnmortgageCost(),
            self.getDiceMultiplierList(),
        )

    def equals(self, other):
        equal = False

        if isinstance(self, Utility) and isinstance(other, Utility):
            if vars(self) == vars(other):
                equal = True
        return equal


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class TrainStation(Property):
    def __init__(
        self,
        pSpaceID,
        pPropertyName,
        pPropertyCost,
        pMortgageValue,
        pUnmortgageCost,
        pOwned,
        pTrainStationRentList,
    ):
        super().__init__(
            pSpaceID, pPropertyName, pPropertyCost, pMortgageValue, pUnmortgageCost, pOwned
        )
        self.trainStationRentList = pTrainStationRentList
        # E.g. Element 0 is with 1 Train Station

    # Accessors ================================================================================================

    def getTrainStationRentList(self):
        return self.trainStationRentList

    # Allows you to select which station rent you want
    def getTrainStationRentItem(self, pIndex):
        return (self.trainStationRentList)[pIndex]

    # Mutators ================================================================================================

    def setTrainStationRentList(self, pTrainStationRentList):
        self.trainStationRentList = pTrainStationRentList

    # Allows you to change the station rent you want
    def setTrainStationRentItem(self, pIndex, pNewTrainStationRent):
        (self.trainStationRentList)[pIndex] = pNewTrainStationRent

    # Other ================================================================================================

    def copyObject(self):
        return TrainStation(
            self.getSpaceID(),
            self.getPropertyName(),
            self.getPropertyCost(),
            self.getMortgageValue(),
            self.getUnmortgageCost(),
            self.getTrainStationRentList(),
        )

    def equals(self, other):
        equal = False

        if isinstance(self, TrainStation) and isinstance(other, TrainStation):
            if vars(self) == vars(other):
                equal = True
        return equal


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class GoSpace(Space):
    def __init__(self, pSpaceID, pLandOnValue, pPassValue):
        super().__init__(pSpaceID)
        self.landOnValue = pLandOnValue
        self.passValue = pPassValue

    # Accessors ================================================================================================

    def getLandOnValue(self):
        return self.landOnValue

    def getPassValue(self):
        return self.passValue

    # Mutators ================================================================================================

    def setLandOnValue(self, pLandOnValue):
        self.landOnValue = pLandOnValue

    def setPassValue(self, pPassValue):
        self.passValue = pPassValue

    # Other ================================================================================================

    def copyObject(self):
        return GoSpace(self.getSpaceID(), self.getLandOnValue(), self.getPassValue())

    def equals(self, other):
        equal = False

        if isinstance(self, GoSpace) and isinstance(other, GoSpace):
            if vars(self) == vars(other):
                equal = True
        return equal


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class JustVisiting(Space):
    def __init__(self, pSpaceID):
        super().__init__(pSpaceID)

    # Accessors ================================================================================================

    # Mutators ================================================================================================

    # Other ================================================================================================

    def copyObject(self):
        return JustVisiting(self.getSpaceID())

    def equals(self, other):
        equal = False

        if isinstance(self, JustVisiting) and isinstance(other, JustVisiting):
            if vars(self) == vars(other):
                equal = True
        return equal


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class FreeParking(Space):
    def __init__(self, pSpaceID):
        super().__init__(pSpaceID)

    # Accessors ================================================================================================

    # Mutators ================================================================================================

    # Other ================================================================================================

    def copyObject(self):
        return FreeParking(self.getSpaceID())

    def equals(self, other):
        equal = False

        if isinstance(self, FreeParking) and isinstance(other, FreeParking):
            if vars(self) == vars(other):
                equal = True
        return equal


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class GoToJail(Space):
    def __init__(self, pSpaceID):
        super().__init__(pSpaceID)

    # Accessors ================================================================================================

    # Mutators ================================================================================================

    # Other ================================================================================================

    def copyObject(self):
        return GoToJail(self.getSpaceID())

    def equals(self, other):
        equal = False

        if isinstance(self, GoToJail) and isinstance(other, GoToJail):
            if vars(self) == vars(other):
                equal = True
        return equal


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class CommunityChestSpace(Space):
    def __init__(self, pSpaceID):
        super().__init__(pSpaceID)

    # Accessors ================================================================================================

    # Mutators ================================================================================================

    # Other ================================================================================================

    def copyObject(self):
        return CommunityChestSpace(self.getSpaceID())

    def equals(self, other):
        equal = False

        if isinstance(self, CommunityChestSpace) and isinstance(
            other, CommunityChestSpace
        ):
            if vars(self) == vars(other):
                equal = True
        return equal


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class ChanceSpace(Space):
    def __init__(self, pSpaceID):
        super().__init__(pSpaceID)

    # Accessors ================================================================================================

    # Mutators ================================================================================================

    # Other ================================================================================================

    def copyObject(self):
        return ChanceSpace(self.getSpaceID())

    def equals(self, other):
        equal = False

        if isinstance(self, ChanceSpace) and isinstance(other, ChanceSpace):
            if vars(self) == vars(other):
                equal = True
        return equal


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class Tax(Space):
    def __init__(self, pSpaceID, pTaxName, pTaxAmount):
        super().__init__(pSpaceID)
        self.taxName = pTaxName
        self.taxAmount = pTaxAmount

    # Accessors ================================================================================================

    def getTaxName(self):
        return self.taxName

    def getTaxAmount(self):
        return self.taxAmount

    # Mutators ================================================================================================

    def setTaxName(self, pTaxName):
        self.taxName = pTaxName

    def setTaxAmount(self, pTaxAmount):
        self.taxAmount = pTaxAmount

    # Other ================================================================================================

    def copyObject(self):
        return Tax(self.getSpaceID(), self.getTaxName(), self.getTaxAmount())

    def equals(self, other):
        equal = False

        if isinstance(self, Tax) and isinstance(other, Tax):
            if vars(self) == vars(other):
                equal = True
        return equal
