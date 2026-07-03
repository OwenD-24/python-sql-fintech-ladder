def format_output(results):
    report_lines = []
    for key in sorted(results.keys()):
        value = results[key]
        report_lines.append(f"{key}: {value}")
    report = "\n".join(report_lines)
    return report

results = {"A": 4, "B": 6, "C": 5}

report = format_output(results)
print(report)