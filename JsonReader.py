import json
from model.OptimizationRun import OptimizationRun


data1 = json.load(open('./Jsons/ALGO_REQUEST_RUNID_32337.json', 'r'))
run1 = OptimizationRun(data1)
