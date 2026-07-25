class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
    def deposit(self,amount,description=''):
        self.ledger.append({'amount':amount,'description':description})
    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount,'description':description})
            return True
        return False
    def get_balance(self):
        balance=0
        for item in self.ledger:
            balance+=item['amount']
        return balance
    def transfer(self,amount,other_category):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {other_category.name}')
            other_category.deposit(amount,f'Transfer from {self.name}')
            return True
        return False
    def check_funds(self,amount):
        return self.get_balance()>=amount
    def __str__(self):
        title=f'{self.name.center(30,"*")}\n'
        items=''
        for item in self.ledger:
            desc=f"{item['description'][:23]:23}"
            amt=f'{item["amount"]:7.2f}'
            items+=f'{desc}{amt}\n'
        total=f'Total: {self.get_balance():.2f}'
        return title+items+total
def create_spend_chart(categories):
    total=0
    percentages=[]
    category_totals=[]
    for category in categories:
        category_spent=0
        for item in category.ledger:
            if item['amount']<0:
                category_spent+=abs(item['amount'])
        category_totals.append(category_spent)
        total+=category_spent
    for spent in category_totals:
        if total>0:
            percentage=(spent/total)*100
            rounded_percentage=int(percentage//10)*10
        else:
            rounded_percentage=0
        percentages.append(rounded_percentage)
    res='Percentage spent by category\n'
    for chart_y in range(100,-1,-10):
        res+=str(chart_y).rjust(3)+'| '
        for p in percentages:
            if p>=chart_y:
                res+='o  '
            else:
                res+='   '
        res+='\n'
    res+='    '+'-'*(len(categories)*3+1)+'\n'
    max_len=max(len(category.name)for category in categories)
    for i in range(max_len):
        res+='     '
        for category in categories:
            if i<len(category.name):
                res+=category.name[i]+'  '
            else:
                res+='   '
        res+='\n'
    return res.rstrip('\n')
