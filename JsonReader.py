import json
from model import OptimizationRun
from utils import OptimizationRunComparator
import sys

data1 = json.load(open(sys.argv[1], 'r'))
run1 = OptimizationRun(data1)

data2 = json.load(open(sys.argv[2] , 'r'))
run2 = OptimizationRun(data2)


OptimizationRunComparator(run1, run2).compare()
