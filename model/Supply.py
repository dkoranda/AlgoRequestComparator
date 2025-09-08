
class Supply:
    """
    A model to represent a supply of assets.
    """
    def __init__(self, supplyId, obligationId, haircut, withdrawalHaircut, concentration,
                 unitOfAllocation, minimumAllocation, price, availableAmount,
                 numberOfMovements, allocationType, derivedSupplySources, pureDerivedSupply,
                 obligationKey, placementCost):
        self.supplyId = supplyId
        self.obligationId = obligationId
        self.haircut = haircut
        self.withdrawalHaircut = withdrawalHaircut
        self.concentration = concentration
        self.unitOfAllocation = unitOfAllocation
        self.minimumAllocation = minimumAllocation
        self.price = price
        self.availableAmount = availableAmount
        self.numberOfMovements = numberOfMovements
        self.allocationType = allocationType
        self.derivedSupplySources = derivedSupplySources
        self.pureDerivedSupply = pureDerivedSupply
        self.obligationKey = obligationKey
        # This will be a list of PlacementCost objects
        self.placementCost = [PlacementCost(**pc) for pc in placementCost]

    def __repr__(self):
        return (f"Supply(supplyId={self.supplyId}, price={self.price}, "
                f"availableAmount={self.availableAmount}, haircut={self.haircut})")

