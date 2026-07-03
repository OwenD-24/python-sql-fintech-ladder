records = ["A:1", "B:2", "A:3"]

for record in records:
    key, value = record.split(":")
    value = int(value)
    print(f"Key: {key}, Value: {value}")


