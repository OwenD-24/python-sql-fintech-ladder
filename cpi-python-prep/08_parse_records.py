record = "TXN001:250:GBP"

parts = record.split(":") # The split method separates the record wherever it finds a colon.

transaction_id = parts[0]
amount = int(parts[1]) # I convert the amount into an integer because split returns strings.
currency = parts[2] # I use list indexes to access each piece.
# The result is a list containing the transaction ID, amount and currency.

print("Transaction ID:", transaction_id)
print("Amount:", amount)    
print("Currency:", currency)

# A system may recieve raw data from a file, API or form.
# It parses that data before validating or storing it.