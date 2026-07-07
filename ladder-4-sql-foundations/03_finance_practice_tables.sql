-- 03_finance_practice_tables.sql
-- Create small FinTech-style practice tables for Ladder 4 SQL foundations.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS validation_errors;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  risk_level TEXT NOT NULL
);

CREATE TABLE accounts (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  account_type TEXT NOT NULL,
  status TEXT NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE transactions (
  id INTEGER PRIMARY KEY,
  account_id INTEGER NOT NULL,
  amount REAL NOT NULL,
  status TEXT NOT NULL,
  transaction_date TEXT NOT NULL,
  FOREIGN KEY (account_id) REFERENCES accounts(id)
);

CREATE TABLE validation_errors (
  id INTEGER PRIMARY KEY,
  transaction_id INTEGER NOT NULL,
  error_type TEXT NOT NULL,
  message TEXT NOT NULL,
  FOREIGN KEY (transaction_id) REFERENCES transactions(id)
);

INSERT INTO customers (id, name, email, risk_level)
VALUES
  (1, 'Ava Carter', 'ava@example.com', 'low'),
  (2, 'Ben Smith', 'ben@example.com', 'medium'),
  (3, 'Cara Jones', 'cara@example.com', 'high');

INSERT INTO accounts (id, customer_id, account_type, status)
VALUES
  (1, 1, 'current', 'active'),
  (2, 1, 'savings', 'active'),
  (3, 2, 'current', 'active'),
  (4, 3, 'current', 'review');

INSERT INTO transactions (id, account_id, amount, status, transaction_date)
VALUES
  (1, 1, 250.00, 'valid', '2026-07-01'),
  (2, 1, -50.00, 'invalid', '2026-07-02'),
  (3, 2, 1000.00, 'valid', '2026-07-02'),
  (4, 3, 0.00, 'invalid', '2026-07-03'),
  (5, 3, 450.00, 'valid', '2026-07-04'),
  (6, 4, 9000.00, 'review', '2026-07-04');

INSERT INTO validation_errors (id, transaction_id, error_type, message)
VALUES
  (1, 2, 'negative_amount', 'Transaction amount cannot be negative.'),
  (2, 4, 'zero_amount', 'Transaction amount cannot be zero.'),
  (3, 6, 'manual_review', 'High-value transaction requires review.');

SELECT *
FROM transactions
ORDER BY transaction_date;