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

    def __eq__(self, other):
        if not isinstance(other, Obligation):
            return False
        print("equals from Obligation")
        # Compare all properties except 'last_modified'
        return (self.obligationAmount == other.obligationAmount and
                self.obligationType == other.obligationType and
                self.obligationPriority == other.obligationPriority
                and self.obligationKey == other.obligationKey)