"""  
- read only --> you can not set the value. Value can not be changed.
- getter --> get a value of a property through a method. Most of the time, you will 
            get the value of a private attribute.
- setter --> set a value of a property through a method. Most of the time, you will 
            set the value of a private property. 
"""

class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    # getter without any setter is readonly attribute
    @property # decorator: akhn ai function ta attribute hishebe kaj korbe. r method thakbe na
    def age(self):
        return self._age
    
    # getter
    @property
    def salary(self):
        return self.__money

    #setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'salary can not be negative'
        self.__money += value

samsu = User('Kopa', 21, 12000)

# print(samsu.__money) # kaj korbe na 
# print(samsu.age()) # akhn kaj korbe
print(samsu.age) # @property decorator use korar por aita kaj korbe
print(samsu.salary)
samsu.salary = 4500
print(samsu .salary)
