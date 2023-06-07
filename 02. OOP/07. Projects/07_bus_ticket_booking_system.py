""" 
 Bus Ticket Booking System
---------------------------

Admin:
    - Add a new bus
    - Check available buses
    - Can check bus info

User:
    - Check available buses
    - Check bus info
    - Can reserve seat
 """

class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(20)] # list --> ["Empty", "Empty", "Empty", ...] evabe 20 ta thakbe

# b = Bus(2, "Nayeem", "12pm", "12:30pm", "Dhaka", "Chittagong") # object
# # print(b) 
# print(vars(b)) # dictionary te represent hoye gelo. akhn bam pasher ta hobe key & dan pasher ta hobe value

class Phitron: # bus company
    total_bus = 5
    total_bus_list = [] # dictionary --> ekhane [{}, {}, {}, ...] evabe info gulo ache

    def add_bus(self):
        bus_no = int(input("Enter Bus No: ")) #admin theke nibo

        flag = 1
        for w in self.total_bus_list:
            if bus_no == w['coach']:
                print("Bus Already Added")
                flag = 0
                break

        if flag: # flag == 1
            bus_driver = input("Enter Bus Driver Name: ")
            bus_arrival = input("Enter Bus Arrival Time: ")
            bus_departure = input("Enter Bus Departure Time: ")
            bus_from = input("Enter Bus Start From: ")
            bus_to = input("Enter Bus Destination: ")

            self.new_bus = Bus(bus_no, bus_driver, bus_arrival, bus_departure, bus_from, bus_to)
            self.total_bus_list.append(vars(self.new_bus)) # dictionary hishebe rakhtechi, jate key-value pair hishebe thake
            print("\nBus Added Successfully!")

# company = Phitron() # object
# company.add_bus()

class Counter(Phitron):
    
    user_list = []

    def reservation(self):
        bus_no = int(input("Enter Bus No: "))

        for w in self.total_bus_list:
            if bus_no == w['coach']:
                passenger = input("Enter Your Name: ")
                seat_no = int(input("Enter Seat No: "))

                if seat_no > 20:
                    print("No seats are available!")
                elif w['seat'][seat_no-1] != "Empty":
                    print("Seat Already Booked!")
                else:
                    w['seat'][seat_no-1] = passenger
                    print(f"Congrats! The {seat_no} no. seat is reserved for  you!")
            else:
                print("No Bus Available!")

        # for bus in self.total_bus_list:
        #      print(bus['seat'])

    def show_ticket(self):
        bus_no = int(input("Enter Bus Number: "))

        for w in self.total_bus_list:
            if bus_no == w['coach']:
                print('*'*50)
                print()
                print(f"{' ' * 10} {'#' * 10} BUS INFO {'#' * 10}")
                print(f"Bus Number : {bus_no} \t\t\t Driver : {w['driver']} ")
                print(f"Arrival : {w['arrival']} \t\t\t Departure Time : {w['departure']} \n From: \t{w['from_des']} \t\t\t To: \t{w['to']}")
                print()
                
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end="\t")
                        a += 1

                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end="\t")
                        a += 1    

                print('*'*50)                           

    def get_user(self):
        return self.user_list

    def create_account(self):
        name = input("Enter Your Username: ")
        password = input("Enter Your Password: ")

        self.new_user = User(name, password)
        self.user_list.append(vars(self.new_user))

    def available_buses(self):
        if len(self.total_bus_list) == 0:
            print("No Buses Available\n")
        else:
            print('*'*50)
            for bus in self.total_bus_list:
                print()
                print(f"{'#' * 10} BUS {bus['coach']} INFO {'#' * 10}")
                print(f"Bus Number : {bus['coach']} \t Driver : {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t Departure Time : {bus['departure']} \n From: \t {bus['from_des']} \t\t To: \t{bus['to']}")
            print('*' * 50)

# company = Phitron()
# company.add_bus()

# counter = Counter()
# counter.reservation()

""" 
For all:
    - Create an account
    - Login to your account
    - exit

Admin:
    - Add Bus
    - Can check available buses
    - Can check bus info
    - exit

User:
    - Can check bus info
    - Reservation / ticket booking
    - Can check available buses
    - exit
"""

while True: 
    company = Phitron()
    b = Counter()
    print("1. Create an account\n2. Login to your account \n3. Exit")

    user_input = int(input("Enter your choice: "))

    if user_input == 3:
        break
    elif user_input == 1:
        b.create_account()
    elif user_input == 2:
        name = input("Enter your username: ")
        password = input("Enter your password: ")

        flag = 0
        isAdmin = False

        if name == "admin" and password == '123':
            isAdmin = True

        if isAdmin == False: # user
            for user in b.get_user():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            
            if flag:
                while True:
                    print(f"\n{' '*10} Welcome to Bus Ticket Booking System!")
                    print("1. Available Buses\n2. Show Bus Info \n3. Reservation \n4. Exit")
                    
                    a = int(input("Enter your choice: "))
                    if a == 4:
                        break
                    elif a == 1:
                        b.available_buses()
                    elif a == 2:
                        b.show_ticket()
                    elif a == 3:
                        b.reservation()
            else:
                print("No username found!")

        else: 
            while True:
                print(f"\n{' ' * 10} Hello Admin! Welcome to Bus Ticket Booking System")
                print("1. Add Bus\n2. Available Buses\n3. Show Bus Info \n4. Exit")

                a = int(input("Enter your choice: "))
                
                if a == 4:
                    break
                elif a == 1:
                    b.add_bus()
                elif a == 2:
                    b.available_buses()
                elif a == 3:
                    b.show_ticket()