from test_fun import *

# perform_data_quality_checks --> rule_engine
# test_fun-->dq_functions


def perform_data_quality_checks(input_table,rule_table,obj_name,src_name,ip_test):

    # Your data quality check logic here

    print(f"Performing data quality checks for tabel {input_table}" )
    print(f"Rule table name is {rule_table}")
    print(f"Object name {obj_name}")
    print(f"Source name {src_name}")
    calling_test(ip_test)
    
    return "function perform successfully!!"