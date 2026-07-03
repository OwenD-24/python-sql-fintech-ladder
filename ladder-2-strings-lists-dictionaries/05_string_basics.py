name = "Owen"
code = "TXN2026"
amount_text = "12000"

print(f"Name lowercase: {name.lower()}")
print(f"Name uppercase: {name.upper()}")
print(f"Is name alphabetic? {name.isalpha()}")
print(f"Is amount numeric? {amount_text.isdigit()}")
print(f"First letter: {name[0]}")
print(f"Last letter: {name[-1]}")
print(f"First three letters: {name[:3]}")
print("Each character in code:")
for char in code:
    print(char)