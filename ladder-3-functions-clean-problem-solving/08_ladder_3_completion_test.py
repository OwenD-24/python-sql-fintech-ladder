def parse_record(record):
    key, value = record.split(":")
    key = key.strip()
    value = value.strip()
    value = int(value)

    return key, value



def group_totals(records):
    totals = {}

    for record in records:
        key, value = parse_record(record)

        if key in totals:
            totals[key] += value
        else:
            totals[key] = value

    return totals



def remove_zero_totals(totals):
    cleaned_totals = {}

    for key, value in totals.items():
        if value != 0:
            cleaned_totals[key] = value
        
    return cleaned_totals



def format_output(results):
    report_lines = []

    for key in sorted(results.keys()):
        value = results[key]
        report_lines.append(f"{key}: {value}")

    report = "\n".join(report_lines)

    return report



records = ["A:1", "B:2", "A:3", "C:0", "B:-2", "D:5", "E:0"]

totals = group_totals(records)
cleaned_totals = remove_zero_totals(totals)
report = format_output(cleaned_totals)

print(report)

