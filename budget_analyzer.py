from datetime import datetime
import math

budget = 0.0
expenses = []
categories = ['Food', 'Travel', 'Shopping', 'Education', 'Others']

def get_amount(message):
    while True:
        try:
            amount = float(input(message))
            if amount > 0 and math.isfinite(amount):
                return amount
            print('Enter a positive, valid amount.')
        except ValueError:
            print('Invalid input. Enter a number.')

def set_budget():
    global budget
    budget = get_amount('Enter monthly budget (Rs.): ')
    print(f'Budget set to Rs. {budget:.2f}')

def add_expense():
    amount = get_amount('Enter expense amount (Rs.): ')
    for i, category in enumerate(categories, 1):
        print(f'{i}. {category}')
    while True:
        try:
            choice = int(input('Enter category number: '))
            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                break
            print('Invalid category.')
        except ValueError:
            print('Enter a valid number.')
    while True:
        date = input('Enter date (DD-MM-YYYY): ')
        try:
            datetime.strptime(date, '%d-%m-%Y')
            break
        except ValueError:
            print('Invalid date. Try again.')
    description = input('Enter description: ')
    expenses.append(dict(amount=amount, category=category, date=date, description=description))
    print('Expense added successfully!')
    if budget > 0:
        budget_alert()

def view_expenses():
    if not expenses:
        print('No expenses recorded.')
        return
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['date']} | {e['category']} | Rs. {e['amount']:.2f} | {e['description']}")

def total_expenses():
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

def category_analysis():
    print('\n--- CATEGORY ANALYSIS ---')
    for category in categories:
        total = 0
        for expense in expenses:
            if expense['category'] == category:
                total += expense['amount']
        print(f'{category}: Rs. {total:.2f}')

def budget_alert():
    if budget <= 0:
        print('Please set your monthly budget first.')
        return
    used = total_expenses() / budget * 100
    if used > 100:
        print('ALERT: Monthly budget exceeded!')
    elif used >= 100:
        print('ALERT: Monthly budget fully used!')
    elif used >= 80:
        print('WARNING: 80% or more of budget used!')
    else:
        print('Spending is within the budget.')

def budget_status():
    if budget <= 0:
        print('Please set your monthly budget first.')
        return
    total = total_expenses()
    print('\n--- BUDGET STATUS ---')
    print(f'Monthly budget: Rs. {budget:.2f}')
    print(f'Total expenses: Rs. {total:.2f}')
    print(f'Remaining budget: Rs. {budget-total:.2f}')
    print(f'Budget used: {total/budget*100:.2f}%')
    budget_alert()

def monthly_summary():
    print('\n--- MONTHLY SUMMARY ---')
    print(f'Number of expenses: {len(expenses)}')
    print(f'Total spent: Rs. {total_expenses():.2f}')
    category_analysis()
    budget_status()

def main():
    while True:
        print('\nPERSONAL EXPENSE & BUDGET ANALYZER')
        print('1. Set Monthly Budget\n2. Add Expense\n3. View Expenses\n4. Category-wise Analysis\n5. Budget Status\n6. Monthly Summary\n7. Exit')
        choice = input('Enter your choice: ')
        if choice == '1': set_budget()
        elif choice == '2': add_expense()
        elif choice == '3': view_expenses()
        elif choice == '4': category_analysis()
        elif choice == '5': budget_status()
        elif choice == '6': monthly_summary()
        elif choice == '7':
            print('Thank you for using Budget Analyzer!')
            break
        else: print('Invalid choice. Select 1 to 7.')

if __name__ == '__main__':
    main()
