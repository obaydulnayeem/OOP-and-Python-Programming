# composition kichuta inheritance er moto. inheritance er kaj tai aktu vinno vabe kore
# composition e 'has a' relation thake, inheritance a 'is a' relation thake
# interview te onk somoy inheritance vs composition shompork ask kore. 

class Engine:
    def __init__(self) -> None:
        pass

    def start(self):
        return "Engine started"

class Driver:
    def __init__(self) -> None:
        pass

# car "has a" engine
class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine()

# Another Example---------------------------------------------------------------
class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self, size) -> None:
        self.size = size

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

# computer 'has a' cpu
# computer 'has a' ram
# computer 'has a' hard drive
class Computer:
    def __init__(self, cores, ram_size, hd_capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disc = HardDrive(hd_capacity)

mac = Computer(8, 16, 512)