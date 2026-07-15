amount = 125.50
currency = "GBP"
supported_currencies = ["GBP", "EUR", "USD"]

assert amount > 0, "Amount should be greater than zero"
assert currency in supported_currencies, "Currency should be supported"

print("All assertions passed.")