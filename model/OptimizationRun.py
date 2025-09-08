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
        
        # Parse the dictionaries of nested objects
        self.obligations = {Obligation(**v) for k, v in optimizationRun['obligations'].items()}
        self.supplies = {Supply(**v) for k, v in optimizationRun['supplies'].items()}
        self.customConstraints = optimizationRun['customConstraints']
        self.optimizationAlgorithmMap =  optimizationRun['optimizationAlgorithmMap']
        
        # Parse the list of nested objects
        # Note: This assumes a simple structure for placements, see the class definition above.
        self.eligibilityMatrix = {k: { x: EligibilityMatrixElement(**y) for x,y in p.items()} for k,p in optimizationRun['eligibilityMatrix'].items()}
        
        

    def __repr__(self):
        return (f"OptimizationRun(id='{self.optimizationRunId}', "
                f"num_obligations={len(self.obligations)}, "
                f"num_supplies={len(self.supplies)})")

