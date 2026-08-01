# A for loop lets me repeat logic over multiple items.
amounts = [100, 0, -25, 10000]

# A for loop repeats logic over each item in a collection.
for amount in amounts:
    if amount <= 0: # An if statement lets the program make a decision.
        print(amount, "Invalid")
    elif amount >= 5000: # elif means otherwise, check this other condition.
        print(amount, "Review")
    else: # Else runs when non of the previous conditions matched.
        print(amount, "Valid")

# This script checks each amount and decides whether it is valid, invalid or needs review.

valid_count = 0
invalid_count = 0
review_count = 0

for amount in amounts:
    if amount <= 0:
        invalid_count += 1
    elif amount >= 5000:
        review_count += 1
    else:
        valid_count += 1

print("Valid count:", valid_count)
print("Invalid count:", invalid_count)
print("Review count:", review_count)

# Loops and conditionals are useful when I need to check multiple records. For example, 
# I can loop through card requests, transactions or report rows, 
# then use if, elif and else to decide whether each record is valid, invalid or needs review.