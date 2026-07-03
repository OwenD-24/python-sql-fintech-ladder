def parse_record(record):
    transaction_id, amount = record.split(":")
    transaction_id = transaction_id.strip()
    amount = amount.strip()
    amount = int(amount)
    return f"{transaction_id} -> {amount}"

result_1 = parse_record("TXN001:250")
result_2 = parse_record("TXN002: 500")
result_3 = parse_record(" TXN003 : 750 ")

print(result_1)
print(result_2)
print(result_3)