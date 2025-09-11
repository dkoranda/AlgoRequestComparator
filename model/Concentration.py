class Concentration:
    def __init__(self, groupName,limit,floor,type,subType,subTypeValue,valuationMeasure,supplyId,obligationId,constraintPriority,isScenarioConcentration):
        self.groupName = groupName
        self.limit = limit
        self.floor = floor
        self.type = type
        self.subtype = subType
        self.subtypevalue = subTypeValue
        self.valuationmeasure = valuationMeasure
        self.supplyid = supplyId
        self.obligaitonId = obligationId
        self.constraintpriority = constraintPriority
        self.isscenarioconcentraion = isScenarioConcentration

    def __eq__(self, other):
        return (self.limit == other.limit and
                self.floor == other.floor and
                self.type == other.type and
                self.subtype == other.subtype and
                self.subtypevalue == other.subtypevalue and
                self.valuationmeasure == other.valuationmeasure and
                self.constraintpriority == other.constraintpriority and
                self.isscenarioconcentraion == other.isscenarioconcentraion)

    def __ne__(self, other):
            return not self.__eq__(other)

    def __hash__(self):
        return hash((self.limit, self.floor, self.type, self.subtype, self.subtypevalue,self.valuationmeasure,self.constraintpriority,self.isscenarioconcentraion))