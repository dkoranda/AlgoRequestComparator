from model.Obligation import Obligation
from model.Supply import Supply
from model.EligibilityMatrixElement import EligibilityMatrixElement

class OptimizationRun:
    """
    The main model representing the entire optimization run data.
    """
    def __init__(self, optimizationRun):
        self.algorithmName = optimizationRun['algorithmName']
        self.optimizationRunId = optimizationRun['optimizationRunId']
        self.synthetic_obligations = []
        self.real_obligations = []
        # Parse the dictionaries of nested objects
        for key,value in optimizationRun['obligations'].items():
            if int(key) < 0:
                self.synthetic_obligations.append(Obligation(**value))
            elif int(key) > 0:
                self.real_obligations.append(Obligation(**value))
        self.obligations = [Obligation(**v) for k, v in optimizationRun['obligations'].items()]
        self.supplies = [Supply(**v) for k, v in optimizationRun['supplies'].items()]
        self.customConstraints = optimizationRun['customConstraints']
        self.optimizationAlgorithmMap =  optimizationRun['optimizationAlgorithmMap']
        
        # Parse the list of nested objects
        # Note: This assumes a simple structure for placements, see the class definition above.
        self.eligibilityMatrix = {k: { x: EligibilityMatrixElement(**y) for x,y in p.items()} for k,p in optimizationRun['eligibilityMatrix'].items()}
        self.sort_obligations()
        self.sort_suplies()
        self.create_position_dict()
        
        

    def __repr__(self):
        return (f"OptimizationRun(id='{self.optimizationRunId}', "
                f"num_obligations={len(self.obligations)}, "
                f"num_supplies={len(self.supplies)})")

    def sort_obligations(self):
        self.synthetic_sorted_obligation = sorted(self.synthetic_obligations,key=lambda x: (x.obligationAmount,x.obligationId))
        self.real_sorted_obligation = sorted(self.real_obligations,key=lambda x: (x.obligationAmount,x.obligationId))

    def sort_suplies(self):
        self.sortedSupplies = sorted(self.supplies,key=lambda x: (x.availableAmount,x.availableQuantity,x.productId))

    def create_position_dict(self):
        self.synth_obligation_id_dict = {value.obligationId:position for position,value in enumerate(self.synthetic_sorted_obligation)}
        self.real_obligation_id_dict = {value.obligationId:position for position,value in enumerate(self.real_sorted_obligation)}
        self.supply_id_dict = {value.supplyId:position for position,value in enumerate(self.sortedSupplies)}
        self.rev_synth_obligation_id_dict = {position:value.obligationId for position,value in enumerate(self.synthetic_sorted_obligation)}
        self.rev_real_obligation_id_dict = {position:value.obligationId for position,value in enumerate(self.real_sorted_obligation)}
        self.rev_supply_id_dict = {position:value.supplyId for position,value in enumerate(self.sortedSupplies)}
        self.synth_index_obligation_dict = {position:value for position,value in enumerate(self.synthetic_sorted_obligation)}
        self.rev_real_obligation_id_dict = {position:value.obligationId for position,value in enumerate(self.real_sorted_obligation)}
        self.real_index_obligation_dict = {position:value for position,value in enumerate(self.real_sorted_obligation)}
        self.rev_supply_dict = {position:value.supplyId for position,value in enumerate(self.sortedSupplies)}
        self.supply_index_dict = {position:value for position,value in enumerate(self.sortedSupplies)}

