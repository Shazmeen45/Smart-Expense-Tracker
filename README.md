
# Smart Expense Tracker

## Project Description

Smart Expense Tracker is a Python-based application that helps users record income and expenses, calculate their remaining balance, search transactions, and view expenses by category. Transaction records are stored in a CSV file.

## Features

- Add income and expenses
- View all transactions
- Calculate total income, expenses, and balance
- Search transactions by category or description
- Delete transactions
- Generate category-wise expense reports
- Save and load transaction records using CSV
- Validate user input and handle common errors

## Technologies Used

- Python
- CSV module
- Object-Oriented Programming
- Git and GitHub
- Visual Studio Code

## Python Concepts Used

- Variables and data types
- Input and output
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- File handling
- Exception handling
- Classes and objects
- Constructors
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction

## Installation and Setup

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

5. Activate the environment on Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

## How to Run

Run the following command in the terminal:

```bash
python main.py
```

Follow the menu options to manage income and expenses.

The application creates `transactions.csv` automatically when transactions are saved.

## Project Structure

```text
Smart-Expense-Tracker/
├── main.py
├── README.md
├── .gitignore
├── transactions.csv
├── screenshots/
└── reports/
```

The CSV file may be excluded from a public repository if it contains personal data.

## Challenges Faced

- Validating transaction amounts and user input
- Saving records so they remain available after restarting the program
- Organizing the application using OOP
- Calculating balances and category-wise expenses correctly

## Future Improvements

- Add transaction dates
- Add monthly reports
- Add charts for expense analysis
- Develop a graphical user interface
- Add budget limits and alerts

## Internship

InternNova — Week 6 Final Python Project

## Author

Student Name: Shazmeen
