#This will be the entry point of your application, 
#handling the user interactions and coordinating the 
#application flow

from data_manager import load_transactions, save_transactions
from models import Transaction, Account

def add_transaction(account):
    date = input("Enter the date of the transaction (YYYY-MM-DD): ")
    category = input("Enter the category of the transaction: ")
    amount = float(input("Enter the amount (negative for expenses, positive for income): "))
    description = input("Enter a description (optional): ")
    transaction = Transaction(date, category, amount, description)
    account.add_transaction(transaction)
    print("Transaction added successfully.")

def main():
    print ("Welcome to the expense tracker")
    account = load_transactions() #loads any existing transactions

    while True:
        print ("\nOptions:")
        print("1: Add a transaction")
        print("2: Show current balance")
        print("3: Exit")
        user_choice = input("Please enter your choice (1, 2, or 3): ")

        if user_choice == '3':
            save_transactions(account) # Save current transactions to account
            print("Transactions saved. Exiting the program.")
            break
        elif user_choice == '1':
            add_transaction(account)
        elif user_choice == '2':
            print(f"Current Balance: ${account.get_balance():.2f}")
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()