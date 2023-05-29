class Shopping:
    def __init__(self, name):
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('total price', total)
        if amount < total:
            print(f'Please provide {total - amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money {extra}')

    def remove_item(self, item):
        for product in self.cart:
            if product['item'] == item:
             self.cart.remove(product)
             break
            else:
             print(f"{item} is not in the cart.")





nayeem = Shopping('O H Nayeem')
nayeem.add_to_cart('alu', 50, 6)
nayeem.add_to_cart('dim', 12, 24)
nayeem.add_to_cart('rice', 50, 5)

print(nayeem.cart)
# nayeem.checkout(600)
# nayeem.checkout(1600)

nayeem.remove_item('dim')
print(nayeem.cart)

nayeem.add_to_cart('dim', 12, 24)
print(nayeem.cart)
