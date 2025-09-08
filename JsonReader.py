import json
from model.OptimizationRun import OptimizationRun

def sortObligations(optimizationRun):
    optimizationRun.sortedObligations = sorted(optimizationRun.obligations,key=lambda x: (x.obligationAmount,x.obligationId))

def sortSuplies(optimizationRun):
    optimizationRun.sortedSupplies = sorted(optimizationRun.supplies,key=lambda x: (x.availableAmount,x.availableQuantity,x.productId))


data1 = json.load(open('./Jsons/ALGO_REQUEST_RUNID_32337.json', 'r'))
run1 = OptimizationRun(data1)

sortObligations(run1)
sortSuplies(run1)
print(run1.sortedObligations)
print(run1.sortedSupplies)