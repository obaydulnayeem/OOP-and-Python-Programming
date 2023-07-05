class Book:
    def __init__(self, name) -> None:
        self.name = name 
    
    def read(self):
        raise NotImplementedError # eta dile baddho hoye implement kortei hobe

class Physics(Book): # subclass   
    def __init__(self, name, lab) -> None:
        self.lab = lab
        super().__init__(name)

topon = Physics('topon', True) # instance

print(issubclass(Physics, Book))
print(isinstance(topon, Physics))
print(isinstance(topon, Book))

topon.read()