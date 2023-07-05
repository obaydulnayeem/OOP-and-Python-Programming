""" 
- static attribute (class attribute)
- static method @staticmethod  --> VVI 
- class method @classmethod
- static method vs class  method
"""

class Shopping:
    cart = [] # class attribute / static attribute
    origin = 'china'

    def __init__(self, name, location) -> None:
        self.name = 'Jamuna City' # instance attribute
        self.location = 'Dhaka' # instance attribute

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')

    @staticmethod
    def multiply(a, b): # static method kore dile r 'self' deya lage na.
        result = a*b
        print(result)

    @classmethod #decorator
    def hudai_dekhi(self, item):
        print('hudai dekhi kintu kinmu na.', item)

basundhara = Shopping('bashundhara', 'dhaka')
# basundhara.purchase('lungi', 500, 1000)
basundhara.hudai_dekhi('lungi')
# Shopping.purchase(2, 3, 3)
Shopping.hudai_dekhi('Lungi')

# basundhara.multiply(4, 5) 
Shopping.multiply(4, 6) # static method. instance chara  

