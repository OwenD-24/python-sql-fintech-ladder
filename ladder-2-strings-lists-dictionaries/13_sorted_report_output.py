totals = {
    "B": 6,
    "A": 4,
    "C": 5
}

report_lines = []

for key in sorted(totals.keys()):
    value = totals[key]
    report_lines.append(f"Key: {key}, Total: {value}") 

report = "\n".join(report_lines)     
print(report)