
# Personal Expense and Budget Analyzer

## Project Overview

The Personal Expense and Budget Analyzer is a menu-driven Python application designed to help students and individuals manage their personal expenses, monitor monthly budgets, and understand their spending habits.

This project was developed as a collaborative academic Python project for Milestone 1 and Milestone 2.

## Problem Statement

Students often struggle to manage their monthly expenses due to a lack of proper expense tracking. This application provides a simple and efficient solution for recording expenses, analyzing expenditure, and monitoring budget utilization.

## Features

- Set a monthly spending budget
- Add expenses with amount, category, date and description
- View recorded expenses
- Analyze category-wise expenditure
- Calculate total expenditure and remaining budget
- Calculate percentage of budget utilized
- Generate warnings at 80% budget utilization
- Generate alerts when the budget is exceeded
- Display monthly expense summary
- Validate user inputs and handle exceptions

## Technologies Used

- Python 3
- Visual Studio Code
- GitHub

## Python Concepts Used

- Variables and data types
- Lists and dictionaries
- Functions
- For and while loops
- Conditional statements
- Exception handling
- Arithmetic operators
- Datetime module
- String formatting

## How to Run the Project

1. Download the budget_analyzer.py file.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

    python3 budget_analyzer.py

On Windows, use python or py if required.

5. Select an operation from the displayed menu.

No external libraries are required.

## Main Menu

    1. Set Monthly Budget
    2. Add Expense
    3. View Expenses
    4. Category-wise Analysis
    5. Budget Status
    6. Monthly Summary
    7. Exit

## Sample Output

    Monthly budget: Rs. 5000.00
    Total expenses: Rs. 11000.00
    Remaining budget: Rs. -6000.00
    Budget used: 220.00%
    ALERT: Monthly budget exceeded!

## Testing

The application was tested for:

- Valid budget and expense inputs
- Expense recording and viewing
- Category-wise calculations
- Monthly summary
- Budget warning and exceeded-budget alerts
- Invalid dates
- Negative amounts
- Non-numeric inputs

## Current Limitations

- Expenses are stored temporarily during execution.
- Data is not retained after closing the program.
- Each session represents one monthly budget period.
- Calendar-month filtering is not implemented.

## Future Scope

- Permanent storage using CSV files or databases
- Graphical user interface
- Spending charts and visualizations
- Monthly expense history
- Expense editing and deletion

## Conclusion

The Personal Expense and Budget Analyzer demonstrates the practical application of fundamental Python programming concepts to solve a real-life financial management problem.

## Project Status

Milestone 1: Completed

Milestone 2 Python Implementation: Completed
