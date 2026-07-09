import sqlite3

database_path = "ladder-6-python-sqlite-workflow/fintech_workflow.sqlite"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM transactions")
valid_transaction_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM validation_errors")
validation_error_count = cursor.fetchone()[0]

cursor.execute("SELECT SUM(amount) FROM transactions")
total_valid_amount = cursor.fetchone()[0]

if total_valid_amount is None:
    total_valid_amount = 0

cursor.execute("""
    SELECT status, COUNT(*) AS total
    FROM transactions
    GROUP BY status
    ORDER BY total DESC
    """)

status_summary = cursor.fetchall()

cursor.execute("""
    SELECT error_message, COUNT(*) AS total
    FROM validation_errors
    GROUP BY error_message
    ORDER BY total DESC
""")

error_summary = cursor.fetchall()

print("FinTech Validation Report")
print("-------------------------")
print("Valid transactions:", valid_transaction_count)
print("Validation errors:", validation_error_count)
print("Total valid amount:", total_valid_amount)

print("\nStatus Summary:")

for status, total in status_summary:
    print(f"{status}: {total}")

print("\nError Summary:")

for error_message, total in error_summary:
    print(f"{error_message}: {total}")

connection.close()