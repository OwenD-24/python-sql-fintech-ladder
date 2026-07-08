import csv

file_path = "ladder-5-python-csv-data-validation/data/transactions.csv"

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)