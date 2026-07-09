import sqlite3

database_path = "ladder-6-python-sqlite-workflow/fintech_workflow.sqlite"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    transaction_id TEXT NOT NULL,
    customer_id TEXT NOT NULL,
    amount REAL NOT NULL,
    currency TEXT NOT NULL,
    date TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS validation_errors (
    id INTEGER PRIMARY KEY,
    transaction_id TEXT,
    error_message TEXT NOT NULL
)
""")

connection.commit()

print("Tables created successfully.")

connection.close()