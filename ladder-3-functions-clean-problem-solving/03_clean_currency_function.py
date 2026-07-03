def clean_currency(value):
    cleaned_value = value.strip().upper()
    if cleaned_value == "GBP" or cleaned_value == "EUR" or cleaned_value == "USD":
        return cleaned_value
    else:
        return "Unsupported"

result_1 = clean_currency(" gbp ")
result_2 = clean_currency("usd")
result_3 = clean_currency(" Eur ")
result_4 = clean_currency(" jpy ")
result_5 = clean_currency("cad")

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)