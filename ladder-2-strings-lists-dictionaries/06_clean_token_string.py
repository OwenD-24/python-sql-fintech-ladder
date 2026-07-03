raw_reference = "TXN-2026#A!B@C"
blocked_characters = ["-", "#", "!", "@"]

cleaned_reference = ""

for char in raw_reference:
    if char not in blocked_characters:
        cleaned_reference += char

print(cleaned_reference)
