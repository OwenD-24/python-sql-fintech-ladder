import csv

file_path = "ladder-5-python-csv-data-validation/data/transactions.csv"

supported_currencies = ["GBP", "EUR", "USD"]
seen_transaction_ids = set()

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        transaction_id = row["transaction_id"]
        currency = row["currency"]

        if currency not in supported_currencies:
            print("Unsupported currency:", row)

        if transaction_id == "":
            continue

        if transaction_id in seen_transaction_ids:
            print("Duplicate transaction ID:", row)
        else:
            seen_transaction_ids.add(transaction_id)