# This script starts with a list of amounts.
amounts = [100, 2050, -50, 700, 0]

# It creates three empty lists: one for valid amounts, one for invalid amounts and one for review amounts.
valid_amounts = []
invalid_amounts = []
review_amounts = []

# The for loop checks each amount one by one.
for amount in amounts:
    if amount <= 0: # If the amount is less than or equal to zero, it gets added to invalid_amounts.
        invalid_amounts.append(amount)
    elif amount >= 500: # If the amount is greater than or equal to 500, it gets added to review_amounts.
        review_amounts.append(amount)
    else: # Otherwise it gets added to valid_amounts.
        valid_amounts.append(amount)

# This is useful in business/data workflows because raw records often need to be separted 
# into valid, invalid and review groups.
print("Valid amounts:", valid_amounts)
print("Invalid amounts:", invalid_amounts)
print("Review amounts:", review_amounts)
print("Number of valid amounts:", len(valid_amounts))
print("Total valid amounts:", sum(valid_amounts))
print("Total review amounts:", sum(review_amounts))

