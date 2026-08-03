transaction = {
    "id": "TXN001",
    "amount": "250" 
} # The transaction dictionary stores an ID and a raw amount value.
# "abc" and an empty string cause ValueError because they are strings that cannot be converted into integers.
# None causes TypeError because it is the wrong type of value.

try: # The try block runs code that might fail.
    amount = int(transaction["amount"]) # int() converts a numeric string into a integer.

    if amount > 0:
        print("Valid")
    else: print("Invalid")

except (ValueError, TypeError): # The except block handles expected errors without crashing the script.
    print("Invalid amount")
# Error handling lets the program return a controlled result for invalid data.