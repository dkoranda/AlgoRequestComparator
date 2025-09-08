class Obligation:
    """
    A model to represent a single obligation.
    """
    def __init__(self, obligationId, obligationAmount, obligationType,
                 obligationPriority, obligationKey):
        self.obligationId = obligationId
        self.obligationAmount = obligationAmount
        self.obligationType = obligationType
        self.obligationPriority = obligationPriority
        self.obligationKey = obligationKey

    def __repr__(self):
        return (f"Obligation(obligationId={self.obligationId}, "
                f"amount={self.obligationAmount})")
