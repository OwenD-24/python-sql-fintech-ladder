import sqlite3

database_path = "ladder-6-python-sqlite-workflow/fintech_workflow.sqlite"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
SELECT transaction_id, customer_id, amount, currency, date, status
FROM transactions
ORDER BY date
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()