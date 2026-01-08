from datetime import datetime
from utils.validators import validate_amount, validate_date, validate_category
from core.expense_manager import (
    add_expense, get_expenses_by_date_range,
    get_total_by_category, delete_expense,
    save_expenses, load_expenses, load_categories
)

# Load existing data
expenses = load_expenses("data/expenses.json")

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses (Date Range)")
    print("3. View Total by Category")
    print("4. Delete Expense")
    print("5. Exit")
    
    choice = input("Choose an option: ").strip()
    
    if choice == "1":
      # Add Expense
        item = input("Item: ").strip()
        
        # Validate amount
        is_valid, result = validate_amount(input("Amount: "))
        if not is_valid:
          print(result)
          continue
        amount = result
        
        # Load categories & Validate category
        categories = load_categories()
        print("Available categories:", ", ".join(categories))
        category_input = input("Category: ").strip()
        is_valid, result = validate_category(category_input, categories)
        if not is_valid:
          print(result)
          continue
        category = result
        
        # Setup time &  Validate date
        date_input = input("Date (YYYY-MM-DD) [Enter for today]: ").strip()
        is_valid, result = validate_date(date_input)
        if not is_valid:
          print(result)
          continue
        date = result
        
        add_expense(expenses, item, amount, category, date)
        print("Expense added!")
        pass
    elif choice == "2":
        # View by date range
        start = input("Start date (YYYY-MM-DD): ").strip()
        end = input("End date (YYYY-MM-DD): ").strip()
        filtered = get_expenses_by_date_range(expenses, start, end)
        for exp in filtered:   
           print(f"- {exp['item']}: ${exp['amount']} on {exp['date']}")
           pass
    elif choice == "3":
        # Total by category
        category = input("Category: ").strip()
        total = get_total_by_category(expenses, category)
        print(f"Total spent on {category}: ${total:.2f}")
        pass
    elif choice == "4":
        # Delete expense
        if not expenses:
            print("No expenses to delete.")
        else:
            print("Current expenses:")
            for exp in expenses:
                print(f"ID {exp['id']}: {exp['item']} - ${exp['amount']} ({exp['date']})")
            try:
                exp_id = int(input("Enter ID to delete: "))
                if delete_expense(expenses, exp_id):
                    print("Expense deleted!")
                else:
                    print("ID not found.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == "5":
        save_expenses(expenses, "data/expenses.json")
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")