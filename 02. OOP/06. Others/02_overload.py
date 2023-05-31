class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def eat(self):
        print('Vat, mangsho, polao, korma')

    def exercise(self):
        raise NotImplementedError 

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self): 
        print('vegetables')

    def exercise(self): 
        print('gym e poisha diya hudai gham jhorai')

    # overloading operators:
    def __add__(self, other): # '+' operator overload
        return self.age + other.age
    
    def __mul__(self, other): # '*' operator overload
        return self.weight * other.weight
    
    def __len__(self): # len overload
        return self.height
    
    def __gt__(self, other): # '>' operator overload
        return self.age > other.age

sakib = Cricketer('Sakib', 38, 68, 91, 'BD')
mushi = Cricketer('mushi', 36, 65, 78, 'BD')


# plus sign overload
print(45 + 98)

print('Sakib' + 'Rakib')

print([12, 39] + [3, 5, 7, 4])

print(sakib + mushi) # upore overload na kora hole eshob operator kaj korto na
print(sakib * mushi)
print(len(sakib))
print(sakib > mushi)