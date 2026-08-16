def validate_amount(amount):
    try:
        amount = int(amount)
    except (ValueError, TypeError):
        return "invalid"
    if amount <= 0:
        return "invalid"
    elif amount >= 5000:
        return "review"
    else:
        return "valid"

def test_review_boundary():
    assert validate_amount(5000) == "review"

def test_valid_boundary():
    assert validate_amount(4999) == "valid"

def test_invalid_format():
    assert validate_amount("abc") == "invalid"

def test_none_input():
    assert validate_amount(None) == "invalid"

def test_valid_amount():
    assert validate_amount(250) == "valid"

def test_invalid_amount():
    assert validate_amount(0) == "invalid"

def test_numeric_string():
    assert validate_amount("250") == "valid"