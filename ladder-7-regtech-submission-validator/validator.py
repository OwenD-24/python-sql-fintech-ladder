import csv
import sqlite3

csv_path = "ladder-7-regtech-submission-validator/data/sample_transactions.csv"
database_path = "ladder-7-regtech-submission-validator/output/submission_results.sqlite"

supported_currencies = ["GBP", "EUR", "USD"]
seen_transaction_ids = set()

valid_rows = []
invalid_rows = []
review_rows = []

with open(csv_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        errors = []

        transaction_id = row["transaction_id"]
        customer_id = row["customer_id"]
        amount_text = row["amount"]
        currency = row["currency"]
        submitted_date = row["submitted_date"]
        source_system = row["source_system"]

        if transaction_id == "":
            errors.append("Missing transaction ID")
        else:
            if transaction_id in seen_transaction_ids:
                errors.append("Duplicate transaction ID")
            else:
                seen_transaction_ids.add(transaction_id)
        
        if customer_id == "":
            errors.append("Missing customer ID")

        if submitted_date == "":
            errors.append("Missing submitted date")

        if currency not in supported_currencies:
            errors.append("Unsupported currency")

        try:
            amount = float(amount_text)

            if amount <= 0:
                errors.append("Invalid amount")

        except ValueError:
            errors.append("Invalid amount format")
            amount = 0

        if len(errors) > 0:
            invalid_rows.append({
                "row": row,
                "errors": errors
            })
        elif amount > 5000:
            review_rows.append(row)
        else:
            valid_rows.append(row)

print("Validation Results")
print("------------------")
print("Valid rows:", len(valid_rows))
print("Review rows:", len(review_rows))
print("Invalid rows", len(invalid_rows))

print("\nInvalid row details:")

for invalid_row in invalid_rows:
    print(invalid_row)

def convert_amount(amount_text):
    try:
        return float(amount_text)
    except ValueError:
        return None


connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS validation_errors")
cursor.execute("DROP TABLE IF EXISTS submission_results")

cursor.execute("""
CREATE TABLE submission_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id TEXT,
    customer_id TEXT,
    raw_amount TEXT,
    amount REAL,
    currency TEXT,
    submitted_date TEXT,
    source_system TEXT,
    result_status TEXT
)
""")

cursor.execute("""
CREATE TABLE validation_errors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id TEXT,
    error_message TEXT NOT NULL
)
""")


def insert_submission(row, result_status):
    cursor.execute("""
    INSERT INTO submission_results (
        transaction_id,
        customer_id,
        raw_amount,
        amount,
        currency,
        submitted_date,
        source_system,
        result_status
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row["transaction_id"],
        row["customer_id"],
        row["amount"],
        convert_amount(row["amount"]),
        row["currency"],
        row["submitted_date"],
        row["source_system"],
        result_status
    ))


for row in valid_rows:
    insert_submission(row, "valid")

for row in review_rows:
    insert_submission(row, "review")

for invalid_item in invalid_rows:
    row = invalid_item["row"]
    errors = invalid_item["errors"]

    insert_submission(row, "invalid")

    error_transaction_id = row["transaction_id"]

    if error_transaction_id == "":
        error_transaction_id = "MISSING_ID"

    for error in errors:
        cursor.execute("""
        INSERT INTO validation_errors (
            transaction_id,
            error_message
        )
        VALUES (?, ?)
        """, (
            error_transaction_id,
            error
        ))

connection.commit()

print("\nSQLite storage complete.")
print("Submission results stored:", len(valid_rows) + len(review_rows) + len(invalid_rows))
print("Validation errors stored:", sum(len(item["errors"]) for item in invalid_rows))

cursor.execute("""
SELECT result_status, COUNT(*) AS total
FROM submission_results
GROUP BY result_status
ORDER BY total DESC
""")

result_summary = cursor.fetchall()

cursor.execute("""
SELECT error_message, COUNT(*) AS total
FROM validation_errors
GROUP BY error_message
ORDER BY total DESC
""")

error_summary = cursor.fetchall()

cursor.execute("""
SELECT source_system, COUNT(*) AS total
FROM submission_results
GROUP BY source_system
ORDER BY total DESC
""")

source_summary = cursor.fetchall()

report_path = "ladder-7-regtech-submission-validator/output/summary_report.txt"

report_lines = [
    "RegTech Submission Validation Report",
    "------------------------------------",
    f"Total submissions: {len(valid_rows) + len(review_rows) + len(invalid_rows)}",
    f"Valid submissions: {len(valid_rows)}",
    f"Review submissions: {len(review_rows)}",
    f"Invalid submissions: {len(invalid_rows)}",
    "",
    "Result summary:"
]

for result_status, total in result_summary:
    report_lines.append(f"{result_status}: {total}")

report_lines.append("")
report_lines.append("Error summary:")

for error_message, total in error_summary:
    report_lines.append(f"{error_message}: {total}")

report_lines.append("")
report_lines.append("Source system summary:")

for source_system, total in source_summary:
    report_lines.append(f"{source_system}: {total}")

with open(report_path, "w") as report_file:
    report_file.write("\n".join(report_lines))

print("\nSummary report")
print("--------------")

for line in report_lines:
    print(line)

print("\nReport written to:", report_path)

connection.close()