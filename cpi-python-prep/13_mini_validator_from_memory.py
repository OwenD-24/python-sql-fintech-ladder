supported_currencies = ("GBP", "USD", "EUR")

transactions = [
    {"id": "TXN001", "amount": 250, "currency": "GBP"},
    {"id": "TXN002", "amount": -50, "currency": "GBP"},
    {"id": "TXN003", "amount": 8000, "currency": "USD"},
    {"id": "TXN002", "amount": 1800, "currency": "EUR"},
    {"id": "", "amount": 800, "currency": "CAD"},
]

valid = []
review = []
invalid = []

seen_ids = set()

# valid, review and invalid start as empty lists because they will store the classified transactions.
# seen_ids starts as an empty set because a set stores unique values and can be used to detect duplicate transaction IDs.

for transaction in transactions:
    errors = []

    transaction_id = transaction["id"]
    amount = transaction["amount"]
    currency = transaction["currency"]
    if not transaction_id:
        errors.append("Missing transaction ID") # If the transaction ID is empty, I add a missing-ID error.
    elif transaction_id in seen_ids:
        errors.append("Duplicate transaction ID") # if the ID is already inside seen_ids, I add a duplicate-ID error.
    else:
        seen_ids.add(transaction_id) # Otherwise, I add the new ID to seen_ids for future duplicate checks.

    if amount <= 0: # The amount rule checks whether the amount is less than or equal to zero.
        errors.append("Amount must be greater than zero") # If it is, an amount error is added.

    if currency not in supported_currencies: # The currency rule checks whether the currency is missing from supported_currencies.
        errors.append("Unsupported currency") # If it is unsupported, a currency error is added.
# These are separate if statements so one transaction can collect multiple errors.

    if errors:
        invalid.append({ # If errors contains any messages, the transaction is invalid.
            "transaction": transaction,
            "errors": errors
        })
    elif amount >= 5000: # If there are no errors but the amount is at least 5000, the transaction needs review.
        review.append(transaction)
    else: # Otherwise, the transaction is valid.
        valid.append(transaction)

# The for loop processes each transaction dictionary one at a time.
# errors starts empty for every transaction so each record gets its own validation results.
# The three variables extract the ID, amount and currency from the current transaction.

print("Valid:", valid)
print("Review:", review)
print("Invalid:", invalid)

print("Valid count:", len(valid))
print("Review count:", len(review))
print("Invalid count:", len(invalid))

# The print statements display the completed valid, review and invalid lists.
# len counts how many transactions are stored in each result list.
# The summary shows one valid transaction, one review transaction and three invalid transactions.