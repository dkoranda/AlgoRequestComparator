from model import OptimizationRun
class OptimizationRunComparator:
    def __init__(self, run1:OptimizationRun, run2:OptimizationRun):
        self.run1 = run1
        self.run2 = run2

    def compare(self):
        size_validation_return_code = self.check_all_sizes()
        if(size_validation_return_code != 0):
            print("Size validation failed")
        positional_obligation_validaiton = self.validate_obligations_positionally()
        if(positional_obligation_validaiton != 0):
            print("oblgiations validation failed")
        cc_validation_return_code = self.validate_custom_constraint()
        if(cc_validation_return_code != 0):
            print("Custom constraint validation failed")
        matrix_validation_code = self.validate_eligibility_matrix()
        if(matrix_validation_code != 0):
            print("Eligibility Matrix validation failed")


    def check_all_sizes(self):
        if(len(self.run1.obligations) != len(self.run2.obligations)):
            print("No of obligations are mistmatched between runs")
            print(f"Run1 has {len(self.run1.obligations)} and run2 has {len(self.run2.obligations)} obligations")
            return -10
        elif (len(self.run1.synthetic_obligations) != len(self.run2.synthetic_obligations)):
            print("No of synthetic obligations are mistmatched between runs")
            print(f"Run1 has {len(self.run1.synthetic_obligations)} and run2 has {len(self.run2.synthetic_obligations)} synthetic obligations")
            return -11
        elif (len(self.run1.supplies) != len(self.run2.supplies)):
            print("No of supplies are mistmatched between runs")
            print(f"Run1 has {len(self.run1.supplies)} and run2 has {len(self.run2.supplies)} supplies")
            return -20
        return 0

    def validate_obligations_positionally(self):
        for synth_obl_key,synth_obl_value in self.run1.synth_index_obligation_dict.items():
            if (synth_obl_value != self.run2.synth_index_obligation_dict[synth_obl_key]):
                return -100
        for real_obl_key,real_obl_value in self.run1.real_index_obligation_dict.items():
            if (real_obl_value != self.run2.real_index_obligation_dict[real_obl_key]):
                return -200

        return 0

    def validate_custom_constraint(self):
        for cc_key,cc_value in self.run1.customConstraints.items():
            if (self.run2.customConstraints[cc_key] == None):
                print(f"Custom constraint {cc_key} does exists in run1 but not in run2")
                return -1000

        for cc_key,cc_value in self.run2.customConstraints.items():
            if (self.run1.customConstraints[cc_key] == None):
                print(f"Custom constraint {cc_key} does exists in run2 but not in run1")
                return -1000

        for cc_key,cc_value in self.run1.customConstraints.items():
            if (cc_value != self.run2.customConstraints[cc_key]):
                print(f"Custom constraint {cc_key} does not match between runs value from run1 is {self.run1.customConstraints[cc_key]} and run2 is {self.run2.customConstraints[cc_key]}")
                return -1000
        return 0

    def validate_eligibility_matrix(self):
        synth_obligation_ids_dict = {obligationId1:self.run2.rev_synth_obligation_id_dict[position] for  obligationId1,position in self.run1.synth_obligation_id_dict.items()}
        real_obligation_ids_dict = {obligationId1:self.run2.rev_real_obligation_id_dict[position] for  obligationId1,position in self.run1.real_obligation_id_dict.items()}
        supply_ids_dict = {supplyId1:self.run2.rev_supply_id_dict[position] for  supplyId1,position in self.run1.supply_id_dict.items()}

        for obligationId1, matrix1 in self.run1.eligibilityMatrix.items():
            if( int(obligationId1) < 0 ):
                matrix2 = self.run2.eligibilityMatrix[str(synth_obligation_ids_dict[int(obligationId1)])]
            else:
                matrix2 = self.run2.eligibilityMatrix[str(real_obligation_ids_dict[int(obligationId1)])]

            if(matrix2 is None):
                print(f" {obligationId1} from run1 has an eligibility matrix but {synth_obligation_ids_dict[obligationId1]} has no eligibility matrix in run2")
                return -2000;

            if( int(obligationId1) > 0 ):
                for supplyId1 , matrixElement1 in matrix1.items():
                    matrixElement2 = matrix2.get(str(supply_ids_dict[int(supplyId1)]))
                    if(matrixElement2 is None):
                        print(f" matrix element for {obligationId1} X {supplyId1} from run1 does not have a mathing element for {synth_obligation_ids_dict[int(obligationId1)]} X {supply_ids_dict[int(supplyId1)]}")
                        return -2000;
                    else:
                        if (matrixElement1 != matrixElement2):
                            print(f" matrix element from run1 for {matrixElement1.obligationId} X {matrixElement1.supplyId} is not matching with run2 for {matrixElement2.obligationId} X {matrixElement2.supplyId}")
                            return -2000;

        synth_obligation_ids_dict2 = {obligationId1:self.run1.rev_synth_obligation_id_dict[position] for  obligationId1,position in self.run2.synth_obligation_id_dict.items()}
        real_obligation_ids_dict2 = {obligationId1:self.run1.rev_real_obligation_id_dict[position] for  obligationId1,position in self.run2.real_obligation_id_dict.items()}

        for obligationId2, matrix2 in self.run2.eligibilityMatrix.items():
            if( int(obligationId2) < 0 ):
                matrix1 = self.run1.eligibilityMatrix[str(synth_obligation_ids_dict2[int(obligationId2)])]
            else:
                matrix1 = self.run1.eligibilityMatrix[str(real_obligation_ids_dict2[int(obligationId2)])]

            if(matrix1 is None):
                print(f" {obligationId2} from run2 has an eligibility matrix but {synth_obligation_ids_dict2[obligationId2]} has no eligibility matrix in run1")
                return -2000;

        return 0
