class BankAccount:
    def __init__(self, account_holder_name, account_number, initial_balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be greater than zero.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance is ${self.balance}.")
            else:
                print("Insufficient funds. Withdrawal cannot be processed.")
        else:
            print("Withdrawal amount must be greater than zero.")
    
    def display_balance(self):
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")

# Example usage:
# Create a bank account
account1 = BankAccount("Alice", "1234567890")

# Deposit and display balance
account1.deposit(1000)
account1.display_balance()

# Withdraw and display balance
account1.withdraw(500)
account1.display_balance()

# Attempt to withdraw more than balance
account1.withdraw(600)
account1.display_balance()
