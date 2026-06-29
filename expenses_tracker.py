"""Expense Tracker Application

Track your daily expenses by category, view totals, and filter by category.
"""

def add_expenses(expenses, amount, category):
    """Add an expense to the list."""
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    """Display all expenses in a formatted way."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\n" + "="*50)
    print(f"{'Amount':<15} {'Category':<20}")
    print("="*50)
    for expense in expenses:
        print(f"${expense['amount']:<14.2f} {expense['category']:<20}")
    print("="*50)

def total_expenses(expenses):
    """Calculate and display total expenses."""
    if not expenses:
        print("No expenses to calculate.")
        return 0
    
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: ${total:.2f}")
    return total

def filter_expenses(expenses, category):
    """Filter and display expenses by category."""
    filtered = [exp for exp in expenses if exp['category'].lower() == category.lower()]
    
    if not filtered:
        print(f"No expenses found for category: {category}")
        return
    
    print(f"\nExpenses in '{category}':")
    print("="*50)
    for expense in filtered:
        print(f"${expense['amount']:<14.2f} {expense['category']:<20}")
    print("="*50)
    category_total = sum(exp['amount'] for exp in filtered)
    print(f"Category Total: ${category_total:.2f}")

def main():
    """Main function to run the expense tracker."""
    expenses = []
    
    while True:
        print('\n' + "="*50)
        print('         EXPENSE TRACKER')
        print("="*50)
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        print("="*50)
        
        choice = input('Enter your choice (1-5): ').strip()
        
        if choice == '1':
            try:
                amount = float(input('Enter the amount: $'))
                if amount < 0:
                    print("Error: Amount cannot be negative!")
                    continue
                category = input('Enter the category: ').strip()
                if not category:
                    print("Error: Category cannot be empty!")
                    continue
                add_expenses(expenses, amount, category)
                print(f"✓ Added ${amount:.2f} to {category}")
            except ValueError:
                print("Error: Please enter a valid amount!")
        
        elif choice == '2':
            print_expenses(expenses)
        
        elif choice == '3':
            total_expenses(expenses)
        
        elif choice == '4':
            category = input('Enter the category to filter: ').strip()
            if not category:
                print("Error: Please enter a category!")
                continue
            filter_expenses(expenses, category)
        
        elif choice == '5':
            print('\nThank you for using Expense Tracker! Goodbye!')
            break
        
        else:
            print("Error: Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
