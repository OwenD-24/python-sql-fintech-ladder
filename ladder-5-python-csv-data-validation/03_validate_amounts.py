import csv

file_path = "ladder-5-python-csv-data-validation/data/transactions.csv"

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        amount_text = row["amount"]
        status = row["status"]

        try:
            amount = float(amount_text)
        except ValueError:
            print("Invalid amount format:", row)
            continue

        if amount <= 0:
            print("Invalid amount:", row)

        if amount > 5000 and status != "review":
            print("Large transaction missing review status:", row)
