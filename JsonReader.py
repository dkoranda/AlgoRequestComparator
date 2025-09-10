import json
from model import OptimizationRun
from utils import OptimizationRunComparator

data1 = json.load(open('./Jsons/ALGO_REQUEST_RUNID_32337.json', 'r'))
run1 = OptimizationRun(data1)

data2 = json.load(open('./Jsons/ALGO_REQUEST_RUNID_32464.json', 'r'))
run2 = OptimizationRun(data2)


OptimizationRunComparator(run1, run2).compare()
