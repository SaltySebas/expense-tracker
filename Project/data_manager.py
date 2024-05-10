#Responsible for file operations
#like reading and writing data to CSV files.
import os
import csv
from models import Transaction, Account

def save_transactions(account, filename='transactions.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for transaction in account.transactions:
            writer.writerow([transaction.date, transaction.category, transacton.amount, transaction.description])



def load_transactions(filename='transactions.csv'):
    account = Account()
    if os.path.exists(filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    transaction = Transaction(date=row[0], category=row[1], amount=float(row[2]), description=row[3])
                    account.add_transaction(transaction)
    else:
        print("No existing transaction file found. Starting a new account.")
    return account