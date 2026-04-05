class Expense:
    def __init__(self, id:int, date:str, amount:float, category:str, description:str):
        self.id = id
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def __repr__(self):
        return f'{self.id} {self.date} {self.amount} {self.category} {self.description}'

class PersonalBudgetTracker:


    def __init__(self):
        self.expenses = []
        self.total = 0.0
        
    def add(self, date, amount, category, description):
        id = int(len(self.expenses) + 1)
        expense = Expense(id, date, amount, category, description)
        self.expenses.append(expense)
        
    def show(self):
        self.expenses.sort(key=lambda e: e.date, reverse=True)
        for expense in self.expenses:
            print(expense)
    
    def filter_by_category(self, filter_str:str):
        filtered = [expense for expense in self.expenses if filter_str.lower() == expense.category.lower()]
        for filter in filtered:
            print(filter)
    def monthly_total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        self.total = total
        print(f'Monthly Total: {self.total}')

    

    
pbt = PersonalBudgetTracker()




# •	"As Lena, I want to type a command to add an expense so I can log it in under 10 seconds." ok

while True:
    command = input("Command: ")
    if command == 'add':
        date = input('Date: ')
        amount = float(input('Amount: '))
        category = input('Category: ')
        description = input('Description: ')
        pbt.add(date, amount, category, description)
        print('\n')

    elif command == 'list':
        pbt.show()

    elif command == 'filter':
        filter_str = str(input('Filter by: '))
        pbt.filter_by_category(filter_str)
    elif command == 'monthly-total':
        pbt.monthly_total()
    elif command == 'exit':
        break


# •	"As Lena, I want to see all expenses sorted by date so I know what I spent recently." ok
# •	"As Lena, I want to filter by category (e.g., Food, Transport) so I can find specific items." ok
# •	"As Lena, I want to see my monthly total so I know if I am over budget." ok




