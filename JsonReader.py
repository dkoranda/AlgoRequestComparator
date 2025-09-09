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
    run.synth_obligation_dict = {value.obligationId:position for position,value in enumerate(run.synthetic_obligations)}
    run.real_obligation_dict = {value.obligationId:position for position,value in enumerate(run.real_obligations)}
    run.supply_dict = {value.supplyId:position for position,value in enumerate(run.supplies)}
    run.rev_synth_position_dict = {position:value.obligationId for position,value in enumerate(run.synthetic_obligations)}
    run.rev_real_obligation_dict = {position:value.obligationId for position,value in enumerate(run.real_obligations)}
    run.rev_supply_dict = {position:value.supplyId for position,value in enumerate(run.supplies)}

def validate_obligations_positionally(run1:OptimizationRun,run2:OptimizationRun):
    for synth_obl_key,synth_obl_value in run1.synth_obligation_dict.items():
        if (synth_obl_key != run2.rev_synth_position_dict[synth_obl_value]):
            return -100
    for real_obl_key,real_obl_value in run1.real_obligation_dict.items():
        if (real_obl_key != run2.rev_real_obligation_dict[real_obl_value]):
            return -100
        
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
print(f"size validation status {size_validation_return_code}")

create_position_dict(run1)
create_position_dict(run2)

positional_obligation_validaiton=validate_obligations_positionally(run1,run2)
print(f"oblgiations validation status {positional_obligation_validaiton}")