SELECT c.customer_name, COUNT(t.transaction_id), SUM(t.amount),
CASE
    WHEN SUM(t.amount) >= 10000 THEN 'high_value'
    ELSE 'standard'
END AS customer_type
FROM customers c
JOIN transactions t
    ON c.customer_id = t.customer_id
WHERE t.status = 'valid'
GROUP BY c.customer_name
ORDER BY SUM(t.amount) DESC;

UPDATE transactions
SET status = 'review'
WHERE amount >= 5000
    AND currency = 'GBP'


SELECT c.customer_name, COUNT(t.transaction_id), SUM(t.amount)
FROM customers c 
JOIN transactions t
    ON c.customer_id = t.customer_id
WHERE t.status = 'valid'
    AND HAVING SUM(t.amount) >= 10000
GROUP BY c.customer_name
ORDER BY SUM(t.amount) DESC; 