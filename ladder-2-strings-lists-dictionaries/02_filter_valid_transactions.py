transaction_amounts = [100, -50, 0, 250, 12000, 500]

valid_amounts = []
invalid_amounts = []
for amount in transaction_amounts:
    if amount > 0:
        valid_amounts.append(amount)
    else:
        invalid_amounts.append(amount)  

print(f"Valid transaction amounts: {valid_amounts}")
print(f"Invalid transaction amounts: {invalid_amounts}")
print(f"Valid count: {len(valid_amounts)}")
print(f"Invalid count: {len(invalid_amounts)}")