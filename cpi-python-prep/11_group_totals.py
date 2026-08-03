# statuses stores a list of status values.
statuses = [
    "valid",
    "invalid",
    "valid",
    "review",
    "valid",
    "invalid"
]

# totals starts as an empty dictionary.
totals = {}

# The for loop processes each status one at a time.
for status in statuses:
    if status in totals: # status in totals checks whether the status already exists as a dictionary key.
        totals[status] += 1 # If the status already exists, it's count increases by one.
    else:
        totals[status] = 1 # If the status does not exist, Python creates it with a starting count of one.

print("Status totals:", totals)

# A dictionary is useful for grouped totals because the key stores the category and the value stores the count.
# The dictionary key stores the status category, and the dictionary value stores its count.