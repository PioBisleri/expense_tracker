import json

# Reads and Loads from the json file
def load_expenses(filename): 
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Saves in the json file
def save_expenses(expenses, filename): 
    with open(filename, 'w') as file:
        json.dump(expenses, file, indent=4) 

# Adds a new expense to the expenses list (does not save to file)
def add_expense(expenses, item, amount, category, date):
    new_expense = {
        "id": len(expenses),
        "item": item,
        "amount": amount,
        "category": category,
        "date": date
    }
    expenses.append(new_expense)

# Gets totals for each category
def get_total_by_category(expenses, category):
    total = 0
    for expense in expenses:
        if expense["category"] == category:
            total += expense["amount"]
    return total

# Deletes an entrie from the expense list (doesn't save)
def delete_expense(expenses, expense_id):
    for i, expense in enumerate(expenses):
        if expense["id"] == expense_id:
            del expenses[i]
            return True  # success
    return False  # not found

# Gets expenses between two dates
def get_expenses_by_date_range(expenses, start_date, end_date):
    filtered = []
    for expense in expenses:
        if start_date <= expense["date"] <= end_date:
            filtered.append(expense)
    return filtered

# Gets total spending between two dates
def get_total_by_date_range(expenses, start_date, end_date):
    filtered = get_expenses_by_date_range(expenses, start_date, end_date)
    total = 0
    for expense in filtered:
        total += expense["amount"]
    return total

# In core/expense_manager.py
def load_categories(filename="data/categories.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return ["Food", "Other"]  # fallback