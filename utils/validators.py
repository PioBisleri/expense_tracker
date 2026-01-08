from datetime import datetime

def validate_amount(amount_str):
    """Validate amount input. Returns (is_valid, value_or_error)."""
    try:
        amount = float(amount_str)
        if amount <= 0:
            return False, "Amount must be positive"
        return True, amount
    except (ValueError, TypeError):
        return False, "Please enter a valid number"

def validate_date(date_str):
    """Validate date input. Empty string = today. Returns (is_valid, date_str)."""
    if not date_str:
        return True, datetime.today().strftime("%Y-%m-%d")
    # Basic format check: YYYY-MM-DD (10 characters)
    if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
        return False, "Date must be YYYY-MM-DD"
    return True, date_str

def validate_category(category, valid_categories):
    """Validate category against allowed list."""
    if category in valid_categories:
        return True, category
    return False, f"Invalid category. Choose from: {', '.join(valid_categories)}"