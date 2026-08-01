# A function is a reusable block of code.
def validate_amount(amount): # A parameter is the input the function recieves.
    if amount <= 0:
        return "invalid" # A return value is the result the function gives back.
    elif amount >= 5000:
        return "review"
    else:
        return "valid"

print(validate_amount(100))
print(validate_amount(0))
print(validate_amount(10000))

amounts = [100, 0, -25, 10000, 250]

for amount in amounts:
    status = validate_amount(amount)
    print(amount, status)

# In this script, validate_amount receives an amount, checks it with if, elif and else, then returns a status.

# A function is useful when I need to resue the same logic in multiple places. 
# For example, I can write a function that takes an amount as a parameter and 
# returns whether it is valid, invalid, or needs review.