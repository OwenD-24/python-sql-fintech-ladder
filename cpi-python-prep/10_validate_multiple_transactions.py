# This uses a list of dictionaries.
transactions = [
    {"id": "TXN001", "amount": 250, "currency": "GBP"},
    {"id": "TXN002", "amount": -50, "currency": "GBP"},
    {"id": "TXN003", "amount": 8000, "currency": "USD"},
] # Each dictionary represents one transaction, and the list stores all the transactions.

valid = []
review = []
invalid = []

# The loop checks each transaction and adds it to the correct result list.
for transaction in transactions:
    if transaction["amount"] <= 0:
        invalid.append(transaction)
    elif transaction["amount"] >= 5000:
        review.append(transaction)
    else:
        valid.append(transaction)

print("Valid:", valid)
print("Review:", review)
print("Invalid:", invalid)