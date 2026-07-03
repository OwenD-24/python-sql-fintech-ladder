message = "FinTech developer"
vowels = "aeiou"
vowel_count = 0

for char in message:
    if char.lower() in vowels:
        vowel_count += 1
        
print(f"Vowel count: {vowel_count}")