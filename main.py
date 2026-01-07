from core.expense_manager import (
    load_expenses, save_expenses, add_expense, 
    get_total_by_category, delete_expense
)

# 1. Load data
expenses = load_expenses("data/expenses.json")

# 2. Add two expenses
add_expense(expenses, "Coffee", 5.0, "Food", "2026-01-08")
add_expense(expenses, "Notebook", 7.5, "Education", "2026-01-08")

# 3. Save
save_expenses(expenses, "data/expenses.json")

# 4. Delete the Notebook (id = 1)
success = delete_expense(expenses, 1)
print("Deletion successful:", success)

# 5. Save again
save_expenses(expenses, "data/expenses.json")

# 6. Check totals
print("Food total:", get_total_by_category(expenses, "Food"))
print("Education total:", get_total_by_category(expenses, "Education"))