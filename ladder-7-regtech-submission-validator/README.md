# RegTech Submission Validator

A Python and SQLite mini project that validates transaction-style submission data against business rules, stores the results, and generates a submission-readiness summary report.

## Project goal

The goal of this project is to mirror a simple RegTech/data-submission workflow:

```txt
sample_transactions.csv
→ Python validation script
→ SQLite database
→ valid / invalid / review results
→ summary report

Features
Reads transaction submission data from CSV
Validates required fields
Checks invalid amount values
Detects duplicate transaction IDs
Flags unsupported currencies
Separates records into valid, invalid, and review groups
Stores results in SQLite
Stores validation error reasons
Generates a summary report
Validation rules

The validator checks for:

Missing transaction ID
Missing customer ID
Missing submitted date
Unsupported currency
Invalid amount format
Amount less than or equal to zero
Duplicate transaction ID
Large submissions requiring review
Tech stack
Python
CSV module
SQLite
SQL queries
File-based report output
Output summary

The current sample dataset produces:

Total submissions: 13
Valid submissions: 3
Review submissions: 2
Invalid submissions: 8

The report also includes:

Result summary
Error summary
Source system summary
Files
data/sample_transactions.csv
validator.py
output/summary_report.txt
How to run

From the repo root:

python .\ladder-7-regtech-submission-validator\validator.py

The script prints the validation summary in the terminal and writes a report to:

ladder-7-regtech-submission-validator/output/summary_report.txt
What this demonstrates

This project demonstrates how Python can automate data validation while SQLite stores and queries structured results. This kind of workflow is useful for FinTech, RegTech, internal tools, reporting checks, and data-quality pipelines.