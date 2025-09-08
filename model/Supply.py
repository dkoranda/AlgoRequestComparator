
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
                f"availableAmount={self.availableAmount}, haircut={self.haircut})")

