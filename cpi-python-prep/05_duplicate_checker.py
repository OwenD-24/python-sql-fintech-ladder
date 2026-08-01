# A set stores unique values.
transaction_ids = ["TXN001", "TXN002", "TXN003", "TXN002"]

# I can use a set to check whether I have already seen something before.
seen_ids = set()
duplicates = []

# In this script, seen_ids stores transaction IDs that have already appeared.
for transaction_id in transaction_ids:
    if transaction_id in seen_ids:
        duplicates.append(transaction_id)
    else:
        seen_ids.add(transaction_id)

# If a transaction ID appears again, it gets added to the duplicates list.
print("Seen IDs:", seen_ids)
print("Duplicates:", duplicates)

# Count the results.
print("Number of unique IDs:", len(seen_ids))
print("Number of duplicate IDs:", len(duplicates))

# A set is useful when I need uniqueness. For example, if I am processing card requests, transactions or report rows, 
# I can use a set to track IDs I have already seen and detect duplicates.