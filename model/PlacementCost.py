class PlacementCost:
    """
    A model to represent the cost associated with a placement.
    """
    def __init__(self, costCategory, cost, costType, costScope):
        self.costCategory = costCategory
        self.cost = cost
        self.costType = costType
        self.costScope = costScope

    def __repr__(self):
        return (f"PlacementCost(costCategory='{self.costCategory}', cost={self.cost}, "
                f"costType='{self.costType}', costScope='{self.costScope}')")
