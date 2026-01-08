from core.expense_manager import (
    load_expenses, save_expenses, add_expense,
    get_expenses_by_date_range, get_total_by_date_range,
    get_total_by_category, delete_expense
)

# Start fresh
expenses = []

# Add test data
add_expense(expenses, "Coffee", 5.0, "Food", "2026-01-05")
add_expense(expenses, "Book", 12.0, "Education", "2026-01-10")
add_expense(expenses, "Lunch", 8.0, "Food", "2026-01-07")

# Test date range filtering
print("=== EXPENSES (Jan 1 – Jan 8) ===")
filtered = get_expenses_by_date_range(expenses, "2026-01-01", "2026-01-08")
for exp in filtered:
    print(f"- {exp['item']} (${exp['amount']}) on {exp['date']}")

total = get_total_by_date_range(expenses, "2026-01-01", "2026-01-08")
print(f"\nTotal spent in period: ${total:.2f}")

# Test category total
food_total = get_total_by_category(expenses, "Food")
print(f"Total on Food: ${food_total:.2f}")