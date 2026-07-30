# A tuple is an ordered, unchangeable collection.
supported_currencies = ("GBP", "USD", "EUR")

currency = "GBP"

if currency in supported_currencies:
    print("Currency supported")
else:
    print("Unsupported currency")


# Fixed card statuses that should no change.
card_statuses = ("active", "blocked", "expired", "pending")

status = "blocked"

if status in card_statuses:
    print("Status allowed")
else:
    print("Status not allowed")


# Lists can change.
amounts = [10, 250, 400]
amounts.append(700)

print("Updated list:", amounts)

# Tuples should not change.
fixed_regions = ("UK", "EU", "US")

print("Fixed regions:", fixed_regions)

# A tuple is like a list, but it cannot be changed after it is created.
# I would use a tuple for fixed values that should not accidentally change, like supported currencies, card statuses, regions or request types.
# In this script, the tuple stores allowed values, and the if statement checks whether the current value is inside that tuple.

# A tuple is useful when I need fixed allowed options. For example, supported currencies or card statuses should stay consistent, so a tuple helps show that those values are not meant to change while the program runs.