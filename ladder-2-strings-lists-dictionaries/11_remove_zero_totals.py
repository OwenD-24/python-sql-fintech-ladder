totals = {
    "A": 4,
    "B": 0,
    "C": 5,
    "D": 0
}

cleaned_totals = {}

for key, value in totals.items():
    if value != 0:
        cleaned_totals[key] = value
print(cleaned_totals)