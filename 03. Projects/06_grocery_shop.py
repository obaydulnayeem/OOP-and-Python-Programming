# not completed yet
# https://docs.google.com/document/d/1oz0kZt1_XdofqfxH0qeiNYTkpUmvLyma0Pdf4CeMkig/edit

class Product:
    def __init__(self, product_name, product_id, price, expired_date) -> None:
        self.product_name = product_name
        self.product_id = product_id
        self.price = price
        self.expire_date = expired_date

    def __repr__(self):
        return f'Product Name: {self.product_name},\n Id: {self.product_id},\n Price: {self.price},\n Expired Date: {self.expire_date}'
    
class Shop: 
    def __init__(self, name, location, propiter, trade_license) -> None:
        self.name = name
        self.location = location
        self.propiter = propiter
        self.trade_license = trade_license

        self.products = []

    def add_product(self, product_name, product_id, price, expired_date): # method
        product = Product(product_name, product_id, price, expired_date)
        self.products.append(product)

    def buy_product(self, product_name, product_id):
        self.product_name = product_name
        self.product_id = product_id

        for product in self.products:
            print(product)

    def __repr__(self):
        shop_info = f'Shop Name:{self.name} \n'

        product_info = ""
        for product in self.products:
            product_info += repr(product)

        return shop_info + product_info

swapno = Shop('Swapno Supar Shop', 'Barishal', 'Nayeem', '645654')
swapno.add_product('Rice', '343', '65', '20.02.2024')

# print(swapno.name)
print(swapno)
swapno.buy_product('Rdice', '657')