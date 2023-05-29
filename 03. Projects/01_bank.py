class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self): # method
        return self.balance
    
    def deposit(self, amount): # method
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount): 
        if amount < self.min_withdraw:
            print(f'you can not withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'you can not withdraw more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'here is your money {amount}. your current balance is {self.get_balance()}')
        
brac = Bank(15000)
brac.withdraw(125)

dbbl = Bank(5000)
dbbl.deposit(2000)
dbbl.deposit(4000)
print(dbbl.get_balance())