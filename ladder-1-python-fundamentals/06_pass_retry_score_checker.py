score = int(input("Enter your score: "))

if score >= 80:
    print(f"Excellent! Your score is {score}")
elif score >= 50:
    print(f"Pass! Your score is {score}")
else:
    print(f"Retry, {score} is below passing score")