What is a list?
- An ordered, changeable collection, which is useful for storing multiple records.

What is a tuple?
- An ordered, unchangeable collection, which is useful for fixed values that shouldn't change like supported currencies.

What is a dictionary?
- Key-value pairs which are useful for representing one structured record with labelled fields.

What is a set?
- Unique values only, which is useful for checking things like duplicate IDs.

When would you use a dictionary instead of a list?
- A dictionary is useful when data needs labelled fields. For example, one transaction can store an ID, amount, and currency using key-value pairs.

How would you check for duplicate IDs?
- I would store previously seen IDs in a set. For each record, I would check whether the ID is already in the set, if it is, it is a duplicate, otherwise I add it to the set.

How would you validate an amount?
- I would first try to convert the amount into a number. Then I would check that it is greater than zero and handle ValueError or TypeError if the input is invalid.

How would you debug a script that crashes?
- I would read the traceback to find the error type and failing line. Then I would check the input, data type, logic and output, fix the cause, and run the script again.

What does a for loop do?
- A for loop repeats code for each item in a collection. For example, it can process each transaction in a list one at a time.

What does a function return?
- A function returns a result back to the code that called it. That result can then be stored in a variable, printed or used elsewhere.

How does you RegTech validator work?
- My RegTech validator reads transaction records from a CSV file and checks them against validation rules. 
- It checks required fields, amount values, date format, supported currencies and duplicate IDs.
- Record with errors are classified as invalid, high-value records can be marked for review, and the remaining records are valid.
- The results are stored in SQLite invalid rows are written to a CSV file, and a summary report shows the final totals.

For a shorter interview version, memorise this:
- My RegTech validator reads transaction data, checks each record against business rules, classifies it as valid, review or invalid, and then stores the results and produces a report.