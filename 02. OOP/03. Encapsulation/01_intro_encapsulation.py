""" 
    encapsulation --> hide details
        Access Modifiers: public, private, protected
"""

class Bank:
    def  __init__(self, holder_name, initial_deposit) -> None:
         self.holder_name = holder_name # public attribute: erokom normal vabe joto attribute declare kora hobe shegulo public hobe
        #self.balance = initial_deposit
         self.__balance = initial_deposit # private: akhn r bahir theke access korte parbe na
         self._branch = 'banani 22' # protected: eta oneke private bole. but etao public

    def deposit(self, amount):
         self.__balance += amount

    def get_balance(self):
         return self.__balance
    
    def withdraw(self, amount):
         if amount < self.__balance:
              return amount
         else:
              return f'Fokira, taka nai!'

rafsun = Bank('Choto Bro', 10000)

print(rafsun.holder_name)
# rafsun.balance = 0
rafsun.deposit(3000)
print(rafsun.get_balance())

rafsun.holder_name = 'Boro Vai'
print(rafsun.holder_name)

# encapsulated kora sotteo access  neyar upay ---------------------------------
# print(dir(rafsun))
# print(rafsun._Bank__balance)