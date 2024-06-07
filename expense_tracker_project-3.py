import csv
from datetime import datetime

# Constants
FILE_NAME = 'expenses.csv'

# Helper functions
def read_expenses():
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def write_expenses(expenses):
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense():
    date = input('Enter date (YYYY-MM-DD): ')
    category = input('Enter category: ')
    amount = input('Enter amount: ')
    description = input('Enter description: ')
    
    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    
    expenses = read_expenses()
    expenses.append(expense)
    write_expenses(expenses)
    print('Expense added successfully!')

def view_expenses():
    expenses = read_expenses()
    if not expenses:
        print('No expenses recorded yet.')
        return

    for expense in expenses:
        print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

def update_expense():
    view_expenses()
    date = input('Enter the date of the expense you want to update (YYYY-MM-DD): ')
    
    expenses = read_expenses()
    for expense in expenses:
        if expense['date'] == date:
            print('Updating expense:')
            print(f"Current category: {expense['category']}")
            expense['category'] = input('Enter new category: ')
            print(f"Current amount: {expense['amount']}")
            expense['amount'] = input('Enter new amount: ')
            print(f"Current description: {expense['description']}")
            expense['description'] = input('Enter new description: ')
            write_expenses(expenses)
            print('Expense updated successfully!')
            return

    print('Expense not found.')

def delete_expense():
    view_expenses()
    date = input('Enter the date of the expense you want to delete (YYYY-MM-DD): ')
    
    expenses = read_expenses()
    new_expenses = [expense for expense in expenses if expense['date'] != date]
    
    if len(expenses) == len(new_expenses):
        print('Expense not found.')
    else:
        write_expenses(new_expenses)
        print('Expense deleted successfully!')

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            update_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
