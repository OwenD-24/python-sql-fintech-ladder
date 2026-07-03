message = "abc xyz!"
shift = 2
alphabet = "abcdefghijklmnopqrstuvwxyz"
encrypted_message = ""

for char in message:
    if char.isalpha():
        old_index = alphabet.index(char)
        new_index = (old_index + shift) % 26
        new_char = alphabet[new_index]
        encrypted_message += new_char
    else:
        encrypted_message += char

print(f"Encrypted message: {encrypted_message}")