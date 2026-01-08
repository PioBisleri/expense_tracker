import tkinter as tk
from tkinter import ttk

class ExpenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("600x400")
        
        # Welcome label
        welcome = ttk.Label(root, text="Welcome to Expense Tracker!", font=("Arial", 16))
        welcome.pack(pady=20)
        
        # Status label
        status = ttk.Label(root, text="GUI components coming soon...")
        status.pack()
        
        # Button frame
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=20)
        
        # Placeholder buttons
        ttk.Button(button_frame, text="Add Expense", command=self.add_expense).pack(side="left", padx=5)
        ttk.Button(button_frame, text="View Expenses", command=self.view_expenses).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Exit", command=root.destroy).pack(side="left", padx=5)
    
    def add_expense(self):
        print("Add expense clicked")  # Will connect to core logic later
    
    def view_expenses(self):
        print("View expenses clicked")  # Will show data later

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseApp(root)
    root.mainloop()