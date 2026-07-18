def parse_record(record):
    try:
        transaction_id, amount = record.split(":")
        transaction_id = transaction_id.strip()
        amount = amount.strip()
        amount = int(amount)

        return f"{transaction_id} -> {amount}"

    except (ValueError, AttributeError):
        return None

assert parse_record("TXN004") is None, "Missing colon should return None"
assert parse_record("TXN005:abc") is None, "Invalid amount should return None"
assert parse_record("") is None, "Emptry record should return None"
assert parse_record(None) is None, "Missing record should return None"
# assert parse_record("TXN001:250") == "TXN001 -> 250"
# assert parse_record("TXN002: 500") == "TXN002 -> 500"
# assert parse_record(" TXN003 : 750 ") == "TXN003 -> 750"

print("All parse_record tests passed.")