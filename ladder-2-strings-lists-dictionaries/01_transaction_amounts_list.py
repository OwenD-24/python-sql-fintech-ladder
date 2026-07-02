transaction_amounts = [100, 200, 300, 400, 500]

print(transaction_amounts)
print(f"Number of transactions: {len(transaction_amounts)}")
print(f"First transactions: {transaction_amounts[0]}")
print(f"Second transactions: {transaction_amounts[1]}")
print(f"last transactions: {transaction_amounts[-1]}")

transaction_amounts[2] = 350 
print(f"Updated third transaction: {transaction_amounts[2]}")
print(transaction_amounts)

transaction_amounts.append(600)
print(f"New amount: {transaction_amounts[-1]}")
print(f"Number of transactions: {len(transaction_amounts)}")