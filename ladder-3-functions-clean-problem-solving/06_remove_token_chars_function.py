def remove_token_chars(text, token):
    cleaned_text = ""
    for char in text:
        if char != token:
            cleaned_text += char
    return cleaned_text

result_1 = remove_token_chars("a-b-c-d", "-")
result_2 = remove_token_chars("TXN#001#ABC", "#")
result_3 = remove_token_chars("1,250,000", ",")

print(result_1)
print(result_2)
print(result_3)