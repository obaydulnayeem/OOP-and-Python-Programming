"""  
Banking Management System
=========================

Create a banking management system where-

User
    - Can create an account.
    - Can deposit and withdrawal amount. 
    - Can check available balance.
    - Can transfer the amount from his account to another user account.
    - Can check transaction history.
    - Can take a loan from the bank twice of his total amount..

Note - User can only withdraw and transfer money from his account if he has money in his account.
If a user is unable to withdraw the amount of money he has deposited in the bank, he will get a message that the bank is bankrupt.

Admin 
    - Can create an account
    - Can check the total available balance of the bank.
    - Can check the total loan amount.
    - Can on or off the loan feature of the bank.
"""

class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, initial_deposit):
        user = User(name, initial_deposit)
        self.users.append(user)
        self.total_balance += initial_deposit
        return user

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False

    def process_loan(self, user, amount):
        if self.loan_feature_enabled and amount <= self.total_balance:
            user.deposit(amount)
            self.total_balance -= amount
            self.total_loan_amount += amount
            return True
        else:
            return False


class User:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.loan_limit = initial_deposit * 2
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
        else:
            print("Insufficient funds")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred {amount} to {recipient.name}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def take_loan(self, amount, bank):
        if bank.process_loan(self, amount):
            self.transaction_history.append(f"Took a loan of {amount}")
        else:
            print("Loan feature is disabled or the bank has insufficient funds for loans")


class Admin(User):
    def __init__(self):
        super().__init__("Admin", 0)

    def process_loan(self, user, amount):
        return True


# Example usage
bank = Bank()
admin = Admin()  # Create an admin user

# Admin actions
bank.create_account("Islami Bank Bank", 450000)
bank.create_account("Krishi Bank", 53400)

admin.deposit(1000)
admin.transfer(500, bank.users[0])
admin.withdraw(200)

print(f"Total bank balance: {bank.get_total_balance()}")
print(f"Total loan amount: {bank.get_total_loan_amount()}")

# User actions
user = bank.create_account("Nayeem", 5100)
user.deposit(200)
user.transfer(300, bank.users[0])
user.withdraw(240)
user.take_loan(1500, bank)

print(f"User balance: {user.get_balance()}")
print(f"User transaction history: {user.transaction_history}")