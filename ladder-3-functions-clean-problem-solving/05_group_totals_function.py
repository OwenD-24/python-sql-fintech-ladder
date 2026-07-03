def group_totals(records):
    totals = {}

    for record in records:
        key, value = record.split(":")
        value = int(value)

        if key in totals:
            totals[key] += value    
        else:
            totals[key] = value

    return totals


records = ["A:1", "B:2", "A:3", "C:5", "B:4"]

result = group_totals(records)

print(result)