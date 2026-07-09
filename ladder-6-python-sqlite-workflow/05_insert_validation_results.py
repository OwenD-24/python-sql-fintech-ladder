import csv
import sqlite3

database_path = "ladder-6-python-sqlite-workflow/fintech_workflow.sqlite"
csv_path = "ladder-5-python-csv-data-validation/data/transactions.csv"

supported_currencies = ["GBP", "EUR", "USD"]
seen_transaction_ids = set()

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("DELETE FROM validation_errors")
cursor.execute("DELETE FROM transactions")

with open(csv_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        errors = []

        transaction_id = row["transaction_id"]
        customer_id = row["customer_id"]
        amount_text = row["amount"]
        currency = row ["currency"]
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
            amount = 0 

        if len(errors) == 0:
            cursor.execute("""
            INSERT INTO transactions (
                transaction_id,
                customer_id,
                amount,
                currency,
                date,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
                transaction_id,
                customer_id,
                amount,
                currency,
                date,
                status
            ))
        else:
            error_transaction_id = transaction_id

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

print("CSV validation results inserted successfully.")

connection.close()