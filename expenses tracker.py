def add_expenses(expenses,amount,category):
    expenses.append({'amount': amount, 'category': category})
def print_expenses(expenses):
    for i in expenses:
        print(f'Amount; {i["amount"]},Category: {i["category"]}')
def total_expenses(expenses):
    sum(map(lambda i:i['amount'],expenses))
def filter_expenses(expenses,category):
        return filter(lambda i:i['category']==category,expenses)
def main():
    expenses=[]
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        choice=input('Enter your choice')
        if choice=='1':
            amount=float(input('enter the amount'))
            category=input('enter the category')
            add_expenses(expenses,amount,category)
        elif choice=='2':
            print('all expenses')
            print_expenses(expenses)
        elif choice=='3':
            print('total expenses')
            total_expenses(expenses)
        elif choice=='4':
            category=input('enter the category to filter')
            print('expenses from {category}')
            filter_by_category=filter_expenses(expenses,category)
            print(filter_by_category)
        elif choice=='5':
            print('exit')
            break
main()
            
