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