import sqlite3 

database_path = "ladder-6-python-sqlite-workflow/fintech_workflow.sqlite"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("DELETE FROM validation_errors")
cursor.execute("DELETE FROM transactions")

sample_transactions = [
    ("TXN001", "CUST001", 250.00, "GBP", "2026-07-01", "valid"),
    ("TXN002", "CUST001", -50.00, "GBP", "2026-07-02", "invalid"),
    ("TXN003", "CUST002", 1000.00, "EUR", "2026-07-02", "valid"),
    ("TXN004", "CUST003", 0.00, "USD", "2026-07-03", "invalid"),
    ("TXN005", "CUST002", 450.00, "GBP", "2026-07-04", "valid"),
    ("TXN006", "CUST004", 9000.00, "GBP", "2026-07-04", "review")
]

cursor.executemany("""
INSERT INTO transactions (
    transaction_id,
    customer_id,
    amount,
    currency,
    date,
    status
)
VALUES (?, ?, ?, ?, ?, ?)
""", sample_transactions)

sample_errors = [
    ("TXN002", "Invalid amount"),
    ("TXN004", "Invalid amount")
]

cursor.executemany("""
INSERT INTO validation_errors (
    transaction_id,
    error_message
)
VALUES (?, ?)
""", sample_errors)

connection.commit()

print("Sample records inserted successfully.")

connection.close()