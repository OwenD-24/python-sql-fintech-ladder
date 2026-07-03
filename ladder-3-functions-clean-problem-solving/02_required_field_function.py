def is_required_field_present(value):
    if value.strip() == "":
        return "Missing"
    else:
        return "Present"
    
result_1 = is_required_field_present("")
result_2 = is_required_field_present("TXN001")
result_3 = is_required_field_present("CUST500")
result_4 = is_required_field_present("  ")

print(result_1)
print(result_2) 
print(result_3)
print(result_4)