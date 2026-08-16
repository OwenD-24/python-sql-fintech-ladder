card_requests = [
    {
        "request_id" : "REQ001",
        "amount" : 250,
        "currency" : "GBP"
    },
    {
        "request_id" : "REQ002",
        "amount" : 6000,
        "currency" : "USD"
    },
    {
        "request_id" : "REQ003",
        "amount" : -200,
        "currency" : "EUR"
    },
    {
        "request_id" : "REQ001",
        "amount" : 100,
        "currency" : "GBP"
    },
    {
        "request_id" : "REQ004",
        "amount" : 500,
        "currency" : "JPY"
    },
    {
        "request_id" : "REQ005",
        "amount" : "abc",
        "currency" : "USD"
    }
]

def amount_validation(amount):
    try:
        amount = int(amount)
    except ValueError:
        return "invalid amount"
    if amount <= 0:
        return "invalid"
    elif amount >= 5000:
        return "review"
    else:
        return "valid"

seen_ids = set()

supported_currencies = ("GBP", "USD", "EUR")

summary_counts = {
    "valid" : 0,
    "review" : 0,
    "invalid" : 0,
    "duplicate" : 0,
    "unsupported currency" : 0
}

for request in card_requests:
    if request["request_id"] in seen_ids:
        print(request["request_id"] + " " + "duplicate")
        summary_counts["duplicate"] += 1
    else:
        seen_ids.add(request["request_id"])
        if request["currency"] not in supported_currencies:
            print(request["request_id"] + " " + "unsupported currency")
            summary_counts["unsupported currency"] += 1
        else: 
            status = amount_validation(request["amount"])
            if status == "valid":
                summary_counts["valid"] += 1
            elif status == "review":
                summary_counts["review"] += 1
            else:
                summary_counts["invalid"] += 1
            print(request["request_id"] + " " + status)

print(summary_counts)