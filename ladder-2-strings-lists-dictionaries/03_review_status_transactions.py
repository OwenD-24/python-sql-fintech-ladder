transaction_amounts = [100, -50, 0, 250, 12000, 500, 15000]
valid_amounts = []
invalid_amounts = []
review_amounts = []

for amount in transaction_amounts:
    if amount <= 0:
        invalid_amounts.append(amount)
    elif amount > 10000:
        review_amounts.append(amount)
    else:
        valid_amounts.append(amount)

print(transaction_amounts)
print(f"Valid amounts: {valid_amounts}")
print(f"Invalid amounts: {invalid_amounts}")
print(f"Review amounts: {review_amounts}")
print(f"Valid count: {len(valid_amounts)}")
print(f"Invalid count: {len(invalid_amounts)}")
print(f"Review count: {len(review_amounts)}")
print(f"Total transactions checked: {len(transaction_amounts)}")