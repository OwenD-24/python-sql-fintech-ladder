import csv

file_path = "ladder-5-python-csv-data-validation/data/transactions.csv"

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        transaction_id = row["transaction_id"]
        customer_id = row["customer_id"]
        date = row["date"]

        if transaction_id == "":
            print("Missing transaction ID:", row)

        if customer_id == "":
            print("Missing customer ID:", row)

        if date == "":
            print("Missing date:", row)

