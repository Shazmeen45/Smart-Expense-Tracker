import csv
import os
from abc import ABC, abstractmethod

FILE_NAME = "transactions.csv"

# Parent class: Abstraction and Encapsulation
class Transaction(ABC):
    def __init__(self, category, amount, description):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.category = category
        self.__amount = amount
        self.description = description

    @property
    def amount(self):
        return self.__amount

    @property
    @abstractmethod
    def transaction_type(self):
        pass

    @abstractmethod
    def calculate_effect(self):
        pass

    def to_dict(self):
        return {
            "type": self.transaction_type,
            "category": self.category,
            "amount": self.amount,
            "description": self.description
        }

# Child class: Inheritance and Polymorphism
class Income(Transaction):
    @property
    def transaction_type(self):
        return "income"

    def calculate_effect(self):
        return self.amount

class Expense(Transaction):
    @property
    def transaction_type(self):
        return "expense"

    def calculate_effect(self):
        return -self.amount

transactions = []

# Create an Income or Expense object from saved data
def create_transaction(data):
    transaction_type = data["type"].lower()
    category = data["category"]
    amount = float(data["amount"])
    description = data["description"]

    if transaction_type == "income":
        return Income(category, amount, description)
    elif transaction_type == "expense":
        return Expense(category, amount, description)

    raise ValueError("Unknown transaction type.")

# Load transactions from CSV
def load_transactions():
    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                transactions.append(create_transaction(row))

    except (OSError, ValueError, KeyError) as error:
        print(f"Could not load transactions: {error}")

# Save transactions to CSV
def save_transactions():
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["type", "category", "amount", "description"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for transaction in transactions:
                writer.writerow(transaction.to_dict())

    except OSError as error:
        print(f"Could not save transactions: {error}")

# Add income or expense
def add_transaction():
    print("\n--- Add Income or Expense ---")

    transaction_type = input(
        "Enter type (income/expense): "
    ).strip().lower()

    if transaction_type not in ["income", "expense"]:
        print("Invalid type! Enter income or expense.")
        return

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount (Rs.): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        description = input("Enter description: ").strip()

        data = {
            "type": transaction_type,
            "category": category,
            "amount": amount,
            "description": description
        }

        transaction = create_transaction(data)
        transactions.append(transaction)
        save_transactions()

        print("Transaction added and saved successfully!")

    except ValueError as error:
        print(f"Invalid input: {error}")

# View all transactions
def view_transactions():
    print("\n--- All Transactions ---")

    if not transactions:
        print("No transactions found.")
        return

    for number, transaction in enumerate(transactions, start=1):
        print(f"\nTransaction #{number}")
        print(f"Type: {transaction.transaction_type.title()}")
        print(f"Category: {transaction.category}")
        print(f"Amount: Rs. {transaction.amount:.2f}")
        print(f"Description: {transaction.description}")

# Display income, expenses and balance
def show_summary():
    total_income = sum(
        t.amount for t in transactions
        if t.transaction_type == "income"
    )

    total_expenses = sum(
        t.amount for t in transactions
        if t.transaction_type == "expense"
    )

    balance = sum(t.calculate_effect() for t in transactions)

    print("\n--- Financial Summary ---")
    print(f"Total Income: Rs. {total_income:.2f}")
    print(f"Total Expenses: Rs. {total_expenses:.2f}")
    print(f"Remaining Balance: Rs. {balance:.2f}")

# Search transactions by category or description
def search_transactions():
    keyword = input(
        "Enter category or description to search: "
    ).strip().lower()

    if not keyword:
        print("Please enter a search keyword.")
        return

    matches = [
        t for t in transactions
        if keyword in t.category.lower()
        or keyword in t.description.lower()
    ]

    if not matches:
        print("No matching transactions found.")
        return

    print("\n--- Search Results ---")

    for number, transaction in enumerate(matches, start=1):
        print(
            f"{number}. {transaction.transaction_type.title()} | "
            f"{transaction.category} | "
            f"Rs. {transaction.amount:.2f} | "
            f"{transaction.description}"
        )

# Delete a transaction and update the CSV
def delete_transaction():
    view_transactions()

    if not transactions:
        return

    try:
        number = int(input("\nEnter transaction number to delete: "))

        if number < 1 or number > len(transactions):
            print("Invalid transaction number.")
            return

        removed = transactions.pop(number - 1)
        save_transactions()

        print(
            f"Deleted: {removed.category} - "
            f"Rs. {removed.amount:.2f}"
        )

    except ValueError:
        print("Please enter a valid whole number.")

# Display expenses grouped by category
def category_expenses():
    expenses_by_category = {}

    for transaction in transactions:
        if transaction.transaction_type == "expense":
            category = transaction.category

            expenses_by_category[category] = (
                expenses_by_category.get(category, 0)
                + transaction.amount
            )

    print("\n--- Expenses by Category ---")

    if not expenses_by_category:
        print("No expenses recorded.")
        return

    for category, amount in expenses_by_category.items():
        print(f"{category}: Rs. {amount:.2f}")

# Main menu
def main():
    load_transactions()

    while True:
        print("\n===== SMART EXPENSE TRACKER =====")
        print("1. Add Income or Expense")
        print("2. View All Transactions")
        print("3. View Financial Summary")
        print("4. Search Transactions")
        print("5. Delete Transaction")
        print("6. Category-wise Expense Report")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            search_transactions()
        elif choice == "5":
            delete_transaction()
        elif choice == "6":
            category_expenses()
        elif choice == "7":
            print("Thank you for using Smart Expense Tracker!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
