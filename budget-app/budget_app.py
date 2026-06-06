# budget_app.py
# Budget category tracker with deposit, withdraw, transfer and balance / Registro de categorías de presupuesto con depósito, retiro, transferencia y saldo
# Includes a spending chart by category / Incluye un gráfico de gastos por categoría

import math

# ─── Category Class / Clase Category ───

class Category:

    # Creates the category with a name and empty ledger / Crea la categoría con un nombre y registro vacío
    def __init__(self, name):
        self.name=name
        self.ledger=[]
        
    # Adds a deposit to the ledger / Añade un depósito al registro
    def deposit(self,amount,description=''):
        self.ledger.append({'amount': amount, 'description': description})
        
    # Adds a withdrawal if there are enough funds / Añade un retiro si hay fondos suficientes
    def withdraw(self,amount,description=''):
        withdrawn=-amount
        if self.check_funds(amount):
            self.ledger.append({'amount': withdrawn, 'description': description})
            return True
        else:
            return False
            
    # Adds up all transactions and returns the balance / Suma todas las transacciones y retorna el saldo
    def get_balance(self):
        total_balance = 0
        for transaction in self.ledger:
            total_balance += transaction['amount']
        return total_balance
        
    # Moves funds from this category to another / Mueve fondos de esta categoría a otra
    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination_category.name}')
            destination_category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    # Returns False if the amount is greater than the balance / Retorna False si el monto es mayor al saldo
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
            
    # Prints the category as a formatted receipt / Muestra la categoría como un recibo formateado
    def __str__(self):
        header = self.name.center(30, '*')
        ledger_body = ''
        for values in self.ledger:
            description = values['description']
            amount = values['amount']
            ledger_body += '\n' + f'{description[:23]:<23}{amount:>7.2f}'
        ending = '\n' + f'Total: {self.get_balance():.2f}'
        return header+ledger_body+ending
        
# ─── Chart Function / Función de gráfico ───

# Builds a bar chart using 'o' markers showing spending per category / Construye un gráfico de barras con marcadores 'o' que muestra el gasto por categoría
def create_spend_chart(categories):

    # Chart's title / Título del gráfico
    chart_title = 'Percentage spent by category'
    
    # Get total withdrawals per category / Obtiene el total de retiros por categoría
    total_spent_list = []
    for category in categories:
        withdrawn_per_category = 0
        for values in category.ledger:
            if values['amount'] < 0:
                withdrawn_per_category += values['amount']
        total_spent_list.append(withdrawn_per_category)
    total_spent=sum(total_spent_list)

    # Round down to nearest 10 as required by the problem / Redondea hacia abajo al múltiplo de 10 según lo pide el enunciado
    percentage_list = []
    for spent_per_category in total_spent_list:
        percentage_per_category = math.floor(spent_per_category/total_spent*10)*10
        percentage_list.append(percentage_per_category)

    # Draw chart rows from 100 to 0 / Dibuja las filas del gráfico de 100 a 0
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

    # Horizontal line below the chart / Línea horizontal debajo del gráfico
    chart_separator = "\n    " + '-' * (len(categories) * 3 + 1)

    # Print category names vertically, one letter per row / Muestra los nombres de categoría verticalmente, una letra por fila
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
