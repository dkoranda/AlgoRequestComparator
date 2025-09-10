import json
from model.OptimizationRun import OptimizationRun

def sort_obligations(optimizationRun):
    optimizationRun.synthetic_sorted_obligation = sorted(optimizationRun.synthetic_obligations,key=lambda x: (x.obligationAmount,x.obligationId))
    optimizationRun.real_sorted_obligation = sorted(optimizationRun.real_obligations,key=lambda x: (x.obligationAmount,x.obligationId))


def sort_suplies(optimizationRun):
    optimizationRun.sortedSupplies = sorted(optimizationRun.supplies,key=lambda x: (x.availableAmount,x.availableQuantity,x.productId))

def check_all_sizes(run1:OptimizationRun,run2:OptimizationRun):
    if(len(run1.obligations) != len(run2.obligations)):
        print("No of obligations are mistmatched between runs")
        print(f"Run1 has {len(run1.obligations)} and run2 has {len(run2.obligations)} obligations")
        return -10
    elif (len(run1.synthetic_obligations) != len(run2.synthetic_obligations)):
        print("No of synthetic obligations are mistmatched between runs")
        print(f"Run1 has {len(run1.synthetic_obligations)} and run2 has {len(run2.synthetic_obligations)} synthetic obligations")
        return -11
    elif (len(run1.supplies) != len(run2.supplies)):
        print("No of supplies are mistmatched between runs")
        print(f"Run1 has {len(run1.supplies)} and run2 has {len(run2.supplies)} supplies")
        return -20
    return 0

def create_position_dict(run:OptimizationRun):
    run.synth_obligation_id_dict = {value.obligationId:position for position,value in enumerate(run.synthetic_sorted_obligation)}
    run.real_obligation_id_dict = {value.obligationId:position for position,value in enumerate(run.real_sorted_obligation)}
    run.supply_id_dict = {value.supplyId:position for position,value in enumerate(run.sortedSupplies)}
    run.rev_synth_obligation_id_dict = {position:value.obligationId for position,value in enumerate(run.synthetic_sorted_obligation)}
    run.rev_real_obligation_id_dict = {position:value.obligationId for position,value in enumerate(run.real_sorted_obligation)}
    run.rev_supply_id_dict = {position:value.supplyId for position,value in enumerate(run.sortedSupplies)}
    run.synth_index_obligation_dict = {position:value for position,value in enumerate(run.synthetic_sorted_obligation)}
    run.rev_real_obligation_id_dict = {position:value.obligationId for position,value in enumerate(run.real_sorted_obligation)}
    run.real_index_obligation_dict = {position:value for position,value in enumerate(run.real_sorted_obligation)}
    run.rev_supply_dict = {position:value.supplyId for position,value in enumerate(run.sortedSupplies)}
    run.supply_index_dict = {position:value for position,value in enumerate(run.sortedSupplies)}


def validate_obligations_positionally(run1:OptimizationRun,run2:OptimizationRun):
    for synth_obl_key,synth_obl_value in run1.synth_index_obligation_dict.items():
        if (synth_obl_value != run2.synth_index_obligation_dict[synth_obl_key]):
            return -100
    for real_obl_key,real_obl_value in run1.real_index_obligation_dict.items():
        if (real_obl_value != run2.real_index_obligation_dict[real_obl_key]):
            return -200
        
    return 0

def validate_custom_constraint(run1:OptimizationRun,run2:OptimizationRun):
    for cc_key,cc_value in run1.customConstraints.items():
        if (cc_value != run2.customConstraints[cc_key]):
            print(f"Custom constraint {cc_key} does not match between runs value from run1 is {run1.customConstraints[cc_key]} and run2 is {run2.customConstraints[cc_key]}")
            return -1000
    return 0

def validate_eligibility_matrix(run1:OptimizationRun,run2:OptimizationRun):
    for obligationId1, matrix1 in run1.eligibilityMatrix.items():
        if( int(obligationId1) < 0 ):
            matrix2 = run2.eligibilityMatrix[run2.rev_synth_obligation_id_dict[run1.synth_obligation_id_dict[obligationId1]]]
        else:
            matrix2 = run2.eligibilityMatrix[run2.rev_real_obligation_id_dict[run1.real_obligation_id_dict[obligationId1]]]
        print(matrix1)
        print(matrix2)
    return 0


data1 = json.load(open('./Jsons/ALGO_REQUEST_RUNID_32337.json', 'r'))
run1 = OptimizationRun(data1)

data2 = json.load(open('./Jsons/ALGO_REQUEST_RUNID_32464.json', 'r'))
run2 = OptimizationRun(data2)


sort_obligations(run1)
sort_suplies(run1)

sort_obligations(run2)
sort_suplies(run2)
size_validation_return_code = check_all_sizes(run1,run2)
if(size_validation_return_code != 0):
    print("Size validation failed")

create_position_dict(run1)
create_position_dict(run2)

positional_obligation_validaiton=validate_obligations_positionally(run1,run2)
if(positional_obligation_validaiton != 0):
    print("oblgiations validation failed")

cc_validation_return_code = validate_custom_constraint(run1,run2)
if(cc_validation_return_code != 0):
    print("Custom constraint validation failed")


eligibility_matrix_return_code=validate_eligibility_matrix(run1,run2)
if(cc_validation_return_code != 0):
    print("Eligibility Matrix validation failed")