from core.expense_manager import load_expenses,save_expenses, add_expense, get_total_by_category, delete_expense

# 1. Load existing expenses
expenses = load_expenses("data/expenses.json")

# 2. Add a test expense
add_expense(expenses, "Notebook", 7.50, "Education", "2026-01-08")
add_expense(expenses, "Coffee", 5, "Food", "2026-01-08")

# 3. Save it
save_expenses(expenses, "data/expenses.json")

# 4. Check totals
food_total = get_total_by_category(expenses, "Food")
edu_total = get_total_by_category(expenses, "Education")

print(f"Total on Food: ${food_total:.2f}")
print(f"Total on Education: ${edu_total:.2f}")