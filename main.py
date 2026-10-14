import json
from pathlib import Path


class ExpenseTracker:
    def __init__(self):
        self.file = "expenses.json"
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if Path(self.file).exists():
            try:
                with open(self.file, "r") as f:
                    self.expenses = json.load(f)
            except (json.JSONDecodeError, OSError):
                self.expenses = []

    def save_expenses(self):
        with open(self.file, "w") as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self):
        try:
            name = input("Enter expense name: ").strip()
            if not name:
                print("Expense name cannot be empty!")
                return

            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero!")
                return

            category = input("Enter category: ").strip()
            date = input("Enter date (DD-MM-YYYY): ").strip()

            expense = {
                "id": max(
                    (item.get("id", 0) for item in self.expenses),
                    default=0
                ) + 1,
                "name": name,
                "amount": amount,
                "category": category,
                "date": date
            }

            self.expenses.append(expense)
            self.save_expenses()
            print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid amount!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found!")
            return

        print("\n========== ALL EXPENSES ==========")

        for expense in self.expenses:
            print(f"\nID: {expense['id']}")
            print(f"Name: {expense['name']}")
            print(f"Amount: Rs. {expense['amount']:.2f}")
            print(f"Category: {expense['category']}")
            print(f"Date: {expense['date']}")

    def search_expense(self):
        keyword = input("Enter expense name to search: ").strip().lower()

        results = [
            expense for expense in self.expenses
            if keyword in expense["name"].lower()
        ]

        if results:
            for expense in results:
                print(expense)
        else:
            print("Expense not found!")

    def delete_expense(self):
        try:
            expense_id = int(input("Enter expense ID to delete: "))

            for expense in self.expenses:
                if expense["id"] == expense_id:
                    self.expenses.remove(expense)
                    self.save_expenses()
                    print("Expense deleted successfully!")
                    return

            print("Expense ID not found!")

        except ValueError:
            print("Please enter a valid ID!")

    def total_expenses(self):
        total = sum(expense["amount"] for expense in self.expenses)
        print(f"Total Expenses: Rs. {total:.2f}")

    def run(self):
        while True:
            print("\n========== EXPENSE TRACKER ==========")
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. Search Expense")
            print("4. Delete Expense")
            print("5. Total Expenses")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.search_expense()
            elif choice == "4":
                self.delete_expense()
            elif choice == "5":
                self.total_expenses()
            elif choice == "6":
                print("Thank you for using Expense Tracker!")
                break
            else:
                print("Invalid choice! Please select 1-6.")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()