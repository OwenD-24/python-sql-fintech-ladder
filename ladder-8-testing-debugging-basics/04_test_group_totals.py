def group_totals(records):
    totals = {}
    try:
        for record in records:
            key, value = record.split(":")
            value = int(value)
            if key in totals:
                totals[key] += value    
            else:
                totals[key] = value
        return totals

    except (ValueError, AttributeError, TypeError):
        return None

records = ["A:1", "B:2", "A:3", "C:5", "B:4"]

result = group_totals(records)

assert result == {
    "A": 4,
    "B": 6,
    "C": 5
}, "Records should be grouped and added correctly"

assert group_totals([]) == {}, "Empty records should return an empty dictionary"
assert group_totals(["A:abc"]) is None, "Non-numeric values should return None"
assert group_totals(["A"]) is None, "Malformed records should return None"
assert group_totals(None) is None, "Missing records should return None"

print("All group_totals tests passed.")