import sqlite3

database_path = "ladder-6-python-sqlite-workflow/fintech_workflow.sqlite"

connection = sqlite3.connect(database_path)

print("SQLite database created or connected successfully.")

connection.close()