-- 04_transactions_sum_invalid_data.sql
-- Practise filtering invalid transaction data and using SUM.

-- Find transactions with invalid amounts.
SELECT id, account_id, amount, status, transaction_date
FROM transactions
WHERE amount <= 0;

-- Count invalid transactions.
SELECT COUNT(*) AS invalid_transaction_count
FROM transactions
WHERE amount <= 0;

-- Sum all valid transaction amounts.
SELECT SUM(amount) AS total_valid_amount
FROM transactions
WHERE status = 'valid';

-- Sum transaction amounts by account.
SELECT account_id, SUM(amount) AS total_amount
FROM transactions
GROUP BY account_id
ORDER BY total_amount DESC;

-- Group validation errors by type.
SELECT error_type, COUNT(*) AS total_errors
FROM validation_errors
GROUP BY error_type
ORDER BY total_errors DESC;