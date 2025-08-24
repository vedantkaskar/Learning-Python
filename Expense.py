import csv
from datetime import datetime
import os


class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                self.expenses = list(reader)
        else:
            # Create file with headers if it doesn't exist
            self.save_expenses()

    def add_expense(self, amount, category, date=None):
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')

        expense = {
            'date': date,
            'amount': amount,
            'category': category
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        if not self.expenses:
            return "No expenses recorded yet."

        return self.expenses

    def calculate_by_category(self):
        totals = {}
        for expense in self.expenses:
            category = expense['category']
            amount = float(expense['amount'])
            totals[category] = totals.get(category, 0) + amount
        return totals

    def save_expenses(self):
        with open(self.filename, 'w', newline='') as file:
            if self.expenses:
                writer = csv.DictWriter(
                    file, fieldnames=self.expenses[0].keys())
                writer.writeheader()
                writer.writerows(self.expenses)
            else:
                writer = csv.DictWriter(
                    file, fieldnames=['date', 'amount', 'category'])
                writer.writeheader()


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Totals by Category")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD) or press enter for today: ")

            if date:
                tracker.add_expense(amount, category, date)
            else:
                tracker.add_expense(amount, category)
            print("Expense added successfully!")

        elif choice == '2':
            expenses = tracker.view_expenses()
            if isinstance(expenses, str):
                print(expenses)
            else:
                for expense in expenses:
                    print(
                        f"Date: {expense['date']}, Amount: ${expense['amount']}, Category: {expense['category']}")

        elif choice == '3':
            totals = tracker.calculate_by_category()
            for category, total in totals.items():
                print(f"{category}: ${total:.2f}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
