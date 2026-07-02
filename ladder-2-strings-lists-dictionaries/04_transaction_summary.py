transaction_amounts = [100, -50, 0, 250, 12000, 500, 15000]
print(f"Original transactions: {transaction_amounts}")

sorted_amounts = sorted(transaction_amounts)
print(f"Sorted transactions: {sorted_amounts}")

smallest_amounts = min(transaction_amounts)
print(f"Smallest transaction: {smallest_amounts}")

largest_amounts = max(transaction_amounts)
print(f"Largest transaction: {largest_amounts}")

total_amount = sum(transaction_amounts)
print(f"Total transaction value: {total_amount}")

transaction_count = len(transaction_amounts)
print(f"Total number of transactions: {transaction_count}")

