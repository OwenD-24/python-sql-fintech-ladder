# A dictionary stores labelled data using key-value pairs.
transaction = {
    "id": "TXN001",
    "amount": 250,
    "currency": "GBP",
    "status": "pending"
}

print(transaction["id"])
print(transaction["amount"])

transaction["status"] = "valid"

print(transaction)

# Add a new key-value pair.
transaction["review_reason"] = "Amount checked"

print(transaction)

# Use the dictionary value to decide the transaction status.
if transaction["amount"] <= 0:
    transaction["status"] = "invalid"
elif transaction["amount"] >= 500:
    transaction["status"] = "review"
else:
    transaction["status"] = "valid"

print("Updated transaction:", transaction)
print("Transaction ID:", transaction["id"])
print("Final status:", transaction["status"])


# A dictionary stores labelled data using keys and values.
# The key is the label, like id, amount, currency or status.
# The value is the actual data stored under that label.
# A dictionary is useful when one record has multiple fields.
# In this script, the dictionary represents one transaction, and I update the status based on the amount.