import math

class Category:
    def __init__(self, name):
        self.name=name
        self.ledger=[]

    def deposit(self,amount,description=''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self,amount,description=''):
        withdrawn=-amount
        if self.check_funds(amount):
            self.ledger.append({'amount': withdrawn, 'description': description})
            return True
        else:
            return False
    
    def get_balance(self):
        total_balance = 0
        for transaction in self.ledger:
            total_balance += transaction['amount']
        return total_balance

    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination_category.name}')
            destination_category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        header = self.name.center(30, '*')
        ledger_body = ''
        for values in self.ledger:
            description = values['description']
            amount = values['amount']
            ledger_body += '\n' + f'{description[:23]:<23}{amount:>7.2f}'
        ending = '\n' + f'Total: {self.get_balance():.2f}'
        return header+ledger_body+ending

def create_spend_chart(categories):
    chart_title = 'Percentage spent by category'
    total_spent_list = []
    for category in categories:
        withdrawn_per_category = 0
        for values in category.ledger:
            if values['amount'] < 0:
                withdrawn_per_category += values['amount']
        total_spent_list.append(withdrawn_per_category)
    total_spent=sum(total_spent_list)

    percentage_list = []
    for spent_per_category in total_spent_list:
        percentage_per_category = math.floor(spent_per_category/total_spent*10)*10
        percentage_list.append(percentage_per_category)
    
    chart_body = ''
    for i in range(100, -1, -10):
        line = '\n' + f'{i:>3}|'
        for percentage in percentage_list:
            if abs(percentage) >= i:
                line += ' o '
            else:
                line += '   '
        line += ' '
        chart_body += line
    
    chart_separator = "\n    " + '-' * (len(categories) * 3 + 1)
    
    lengths = []
    for category in categories:
        lengths.append(len(category.name))
    max_length = max(lengths)

    tag_lines = ''
    for number_of_letter in range(max_length):
        line= '\n     '
        for category in categories:
            if number_of_letter >= len(category.name):
                line += '   '
            else:
                line += category.name[number_of_letter] + '  '
        tag_lines += line

    return chart_title + chart_body + chart_separator + tag_lines
