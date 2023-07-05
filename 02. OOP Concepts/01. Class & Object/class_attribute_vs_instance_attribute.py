""" Example-2: Class Attribute ================================================================="""
# class Shop:
#    cart = [] # this 'cart' is a class attribute

#    def __init__(self, buyer): 
#       self.buyer = buyer

#    def add_to_cart(self, item):
#       self.cart.append(item)

# nayeem = Shop('Nayeem')
# nayeem.add_to_cart('Shoes')
# nayeem.add_to_cart('phone')
# print(nayeem.cart)

# tanvir = Shop('Tanvir')
# tanvir.add_to_cart('pen')
# tanvir.add_to_cart('book')
# print(tanvir.cart) # limitation: nayeem er gulo o print hocche. 

""" Instance Attribute =================================================== """
class Shop2:
   shopping_mall = 'Jamuna'
   def __init__(self, buyer):
      self.buyer = buyer
      self.cart = [] # this 'cart' is an instance attribute

   def add_to_cart(self, item):
      self.cart.append(item)

nayeem = Shop2('O H Nayeem')
nayeem.add_to_cart('shoes')
nayeem.add_to_cart('book')
print(nayeem.cart)

tanvir = Shop2('Tanvir')
tanvir.add_to_cart('pen')
tanvir.add_to_cart('mobile')
print(tanvir.cart)