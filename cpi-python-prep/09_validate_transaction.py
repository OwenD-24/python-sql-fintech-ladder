# supported_currencies stores the currency values accepted by the system.
supported_currencies = ("GBP", "USD", "EUR")

# The transaction dictionary represents one transaction using labelled fields.
transaction = {
    "id": "TXN001",
    "amount": -50,
    "currency": "CAD"
}

# errors starts as an empty list so validation messages can be collected.
errors = []

if transaction["amount"] <= 0: # The amount rule checks whether the amount is less than or equal or equal to zero.
    errors.append("Amount must be greater than zero")

if transaction["currency"] not in supported_currencies: # The currency rule checks whether the currency is missing frm supported_currencies.
    errors.append("Unsupported currency")

if errors: # if errors checks whether any validation messages were added.
    print("Invalid:", errors)
else:
    print("Valid")
# If errors exist, the transaction is invalid. Otherwise, it is valid.