# parent class er method child class e korlei override

class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def eat(self):
        print('Vat, mangsho, polao, korma')

    def exercise(self):
        raise NotImplementedError # eta dile override kortei hobe. noyto kaj korbe na.

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self): # override -> uporer 'eat' function er poriborte akhn aita kaj korbe
        print('vegetables')

    def exercise(self): # override -> uporer 'exercise' function er poriborte akhn aita kaj korbe
        print('gym e poisha diya hudai gham jhorai')

sakib = Cricketer('Sakib', 38, 68, 91, 'BD')
# sakib.eat() 
# sakib.exercise()