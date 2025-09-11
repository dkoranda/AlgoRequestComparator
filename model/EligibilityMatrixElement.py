from model.Concentration import Concentration
from model.PlacementCost import PlacementCost

class EligibilityMatrixElement:
    def __init__(self,supplyId,obligationId,haircut,withdrawalHaircut,concentration,
                 unitOfAllocation,minimumAllocation,price,availableAmount,numberOfMovements,allocationType,
                 derivedSupplySources, pureDerivedSupply,obligationKey,placementCost):
        self.supplyId = supplyId
        self.obligationId = obligationId
        self.haircut = haircut
        self.withdrawalHaircut = withdrawalHaircut
        self.unitOfAllocation = unitOfAllocation
        self.minimumAllocation = minimumAllocation
        self.price = price
        self.availableAmount = availableAmount
        self.numberOfMovements = numberOfMovements
        self.allocationType = allocationType
        self.derivedSupplySources = derivedSupplySources
        self.pureDerivedSupply = pureDerivedSupply
        self.obligationKey = obligationKey
        self.placementCost = [PlacementCost(**c) for c in placementCost]
        self.concentration = [Concentration(**c) for c in concentration]

    def __eq__(self, other):
        if not isinstance(other, EligibilityMatrixElement):
            return False
            # Compare all properties except 'last_modified'
        return (self.haircut == other.haircut
                and self.withdrawalHaircut == other.withdrawalHaircut
                and self.concentration == other.concentration
                and self.placementCost == other.placementCost
                and self.minimumAllocation == other.minimumAllocation
                and self.price == other.price
                and self.availableAmount == other.availableAmount
                and self.numberOfMovements == other.numberOfMovements
                and self.allocationType == other.allocationType
                and self.derivedSupplySources == other.derivedSupplySources
                and self.pureDerivedSupply == other.pureDerivedSupply
                and self.obligationKey == other.obligationKey)




