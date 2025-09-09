
class Supply:
    """
    A model to represent a supply of assets.
    """
    def __init__(self, supplyId,availableAmount, availableQuantity, productId, price, numberOfMovementsToBox):
        self.supplyId = supplyId
        self.availableAmount = availableAmount
        self.availableQuantity = availableQuantity
        self.productId = productId
        self.price = price
        self.numberOfMovementsToBox = numberOfMovementsToBox

    def __repr__(self):
        return (f"Supply(supplyId={self.supplyId}, price={self.price}, "
                f"availableAmount={self.availableAmount}, availableQuantity={self.availableQuantity},"
                f" productId={self.productId}, price={self.price}")

    def __eq__(self, other):
        if not isinstance(other, Supply):
            return False
        
        # Compare all properties except 'last_modified'
        return (self.availableAmount == other.availableAmount and
                self.availableQuantity == other.availableQuantity and
                self.price == other.price
                and self.productId == other.productId)
