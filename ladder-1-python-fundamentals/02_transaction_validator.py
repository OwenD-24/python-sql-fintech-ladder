amount = int(input("Enter transaction amount: "))

if amount <= 0:
    status = "Invalid"
elif amount > 10000:
    status = "Review"
else:
    status = "Valid"

print(f"Transaction status: {status}")