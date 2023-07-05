from menu import Pizza, Burger, Drinks, Menu
from restaurant import Restaurant
from users import Chef, Customer, Server, Manager
from order import Order

def main():
    menu = Menu()
    
    # add pizza to the menu
    pizza_1 = Pizza('Shutki Pizza', 500, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)

    pizza_2 = Pizza('Alu Vorta Pizza', 499, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)

    pizza_3  = Pizza('Dal Pizza', 500, 'large', ['dal', 'oil'])
    menu.add_menu_item('pizza', pizza_3)

    # add burger to the menu
    burger_1 = Burger('Nega Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)

    burger_2 = Burger('Beef Burger', 1200, 'beef', ['goru', 'haddi'])
    menu.add_menu_item('burger', burger_2)

    # add drinks to the menu
    coke = Drinks('Coke', 50, True)
    menu.add_menu_item('drink', coke)
    coffee = Drinks('Mocha Coffe', 200, False)
    menu.add_menu_item('drink', coffee)

    # show menu
    # menu.show_menu()

    # make restaurant
    restaurant = Restaurant('Barishal King Restaurant', 2000, menu)
    
    # add employees
    manager = Manager('Kala Chan Manager', 434323465, 'kala@gmail.com', 'kaliapur', 1500, 'jan 1 2020', 'core')
    restaurant.add_employee('manager', manager)

    chef = Chef('Rustum Baburchi', 643534, 'chup@gmail.com', 'rustumnagar', 3543, 'feb 2 2020', 'chef', 'everything')
    restaurant.add_employee('chef', chef)

    server = Server('Chotu Server', 45434, 'nai@jai.com', 'restaurant', 300, 'march 1 2020', 'server')
    restaurant.add_employee('server', server) 

    # show employees
    # restaurant.show_employees()

    # customer_1 placing an order_1
    customer_1 = Customer('Sakib Khan', 454353, 'king@gmail.com', 'banani', 10000)
    order_1 = Order(customer_1, [pizza_3, coffee])
    customer_1.pay_for_order(order_1) 
    restaurant.add_order(order_1)

    # customer_1 paying for order_1
    restaurant.receive_payment(order_1, 2000, customer_1)

    print('revenue and balance after custermer-1', restaurant.revenue, restaurant.balance)

    # customer_2 placing an order_2
    customer_2 = Customer('Rakib Khan', 454353, 'king@gmail.com', 'banani', 10000)
    order_2 = Order(customer_2, [pizza_1, burger_2, coffee])
    customer_2.pay_for_order(order_2) 
    restaurant.add_order(order_2)

    # customer_1 paying for order_1
    restaurant.receive_payment(order_2, 3000, customer_2)

    print('revenue and balance after custermer-2', restaurant.revenue, restaurant.balance)

    # pay rent
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print('after rent', restaurant.revenue, restaurant.balance, restaurant.expense)

    # pay salary
    restaurant.pay_salary(chef)
    print('after salary', restaurant.revenue, restaurant.balance, restaurant.expense) # balance vul dekhacche


if __name__ == '__main__':
    main()