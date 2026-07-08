import csv

file_path = "ladder-5-python-csv-data-validation/data/transactions.csv"

supported_currencies = ["GBP", "EUR", "USD"]
seen_transaction_ids = set()

valid_rows = []
invalid_rows = []

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        errors = []

        transaction_id = row["transaction_id"]
        customer_id = row["customer_id"]
        amount_text = row["amount"]
        currency = row["currency"]
        date = row["date"]
        status = row["status"]

        if transaction_id == "":
            errors.append("Missing transaction ID")
        else:
            if transaction_id in seen_transaction_ids:
                errors.append("Duplicate transaction ID")
            else:
                seen_transaction_ids.add(transaction_id)

        if customer_id == "":
            errors.append("Missing customer ID")

        if date == "":
            errors.append("Missing date")

        if currency not in supported_currencies:
            errors.append("Unsupported currency")

        try:
            amount = float(amount_text)

            if amount <= 0:
                errors.append("Invalid amount")

            if amount > 5000 and status != "review":
                errors.append("Large transaction missing review status")

        except ValueError:
            errors.append("Invalid amount format")

        if len(errors) == 0:
            valid_rows.append(row)
        else:
            invalid_rows.append({
                "row": row,
                "errors": errors
            })

print("Validation Summary")
print("------------------")
print("Total rows:", len(valid_rows) + len(invalid_rows))
print("Valid rows:", len(valid_rows))
print("Invalid rows:", len(invalid_rows))

print("\nInvalid row details:")

for invalid_row in invalid_rows:
    print(invalid_row)