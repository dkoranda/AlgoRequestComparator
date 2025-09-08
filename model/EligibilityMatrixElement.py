import PlacementCost

class EligibilityMatrixElement:
    def __init__(self,eligibilityMatrixElement: dict):
        self.supplyId = eligibilityMatrixElement['supplyId']
        self.obligationId = eligibilityMatrixElement['supplyId']
        self.haircut = eligibilityMatrixElement['supplyId']
        self.withdrawalHaircut = eligibilityMatrixElement['supplyId']
        self.concentration = eligibilityMatrixElement['supplyId']
        self.unitOfAllocation = eligibilityMatrixElement['supplyId']
        self.minimumAllocation = eligibilityMatrixElement['supplyId']
        self.price = eligibilityMatrixElement['supplyId']
        self.availableAmount = eligibilityMatrixElement['supplyId']
        self.numberOfMovements = eligibilityMatrixElement['supplyId']
        self.allocationType = eligibilityMatrixElement['supplyId']
        self.derivedSupplySources = eligibilityMatrixElement['supplyId']
        self.pureDerivedSupply = eligibilityMatrixElement['supplyId']
        self.obligationKey = eligibilityMatrixElement['supplyId']
        self.placementCost = [PlacementCost(**c) for c in eligibilityMatrixElement['placementCost']]