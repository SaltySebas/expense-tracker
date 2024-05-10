#This module will define classes such as Transaction and
#Account to manage the financial data.

class Transaction:
    def __init__(self, date, category, amount, description=''):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


class Account: 
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        return sum(t.amount for t in self.transactions)