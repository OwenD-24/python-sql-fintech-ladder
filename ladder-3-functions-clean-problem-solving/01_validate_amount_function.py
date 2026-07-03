def validate_amount(amount):
    if amount <= 0:
        return "Invalid"
    elif amount > 10000:
        return "Review"
    else:
        return "Valid"

result_1 = validate_amount(-50)
result_2 = validate_amount(500)
result_3 = validate_amount(15000)

print(result_1)
print(result_2)
print(result_3)