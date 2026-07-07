-- 05_customers_accounts_join.sql
-- Practise basic JOIN queries with customers, accounts and transactions.

-- Join customers to accounts.
SELECT customers.name, accounts.account_type, accounts.status
FROM customers
JOIN accounts
ON customers.id = accounts.customer_id
ORDER BY customers.name;

-- Join accounts to transactions.
SELECT accounts.id AS account_id, accounts.account_type, transactions.amount, transactions.status
FROM accounts
JOIN transactions
ON accounts.id = transactions.account_id
ORDER BY transactions.transaction_date;

-- Join customers, accounts and transactions together.
SELECT
  customers.name,
  accounts.account_type,
  transactions.amount,
  transactions.status,
  transactions.transaction_date
FROM customers
JOIN accounts
ON customers.id = accounts.customer_id
JOIN transactions
ON accounts.id = transactions.account_id
ORDER BY transactions.transaction_date;