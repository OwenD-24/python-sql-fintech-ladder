import sqlite3

database_path = "ladder-6-python-sqlite-workflow/fintech_workflow.sqlite"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
SELECT transaction_id, error_message
FROM validation_errors
ORDER BY transaction_id
""")

invalid_records = cursor.fetchall()

print("Invalid Records")
print("---------------")

for record in invalid_records:
    print(record)

connection.close()