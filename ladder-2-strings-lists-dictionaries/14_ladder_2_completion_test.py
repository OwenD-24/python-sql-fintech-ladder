records = ["A:1", "B:2", "A:3", "C:0", "B:-2", "D:5", "E:0"]

totals = {}

for record in records:
    key, value = record.split(":")
    value = int(value)

    if key in totals:
        totals[key] += value
    else:
        totals[key] = value


cleaned_totals = {}

for key, value in totals.items():
    if value != 0:
        cleaned_totals[key] = value


report_lines = []

for key in sorted(cleaned_totals.keys()):
    value = cleaned_totals[key]
    report_lines.append(f"{key}: {value}")

report = "\n".join(report_lines)
print(report) 