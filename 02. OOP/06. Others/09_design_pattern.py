""" 
    - valo programmer hote gele design pattern jantei hobe


    Important Types: 
        - creational patterns
            - singleton
            - factory
            - builder

        - structural patterns
            - adapter
            - facade
        
        - behavioral patterns
            - observer
            - state

    Websites:
        - https://www.dofactory.com/net/design-patterns 
        - https://refactoring.guru/design-patterns
        - 
    Books:
        - https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612
        - Code Complete
"""

#---Singleton Design Pattern=======================================================

# singleton --> akta single instance thakbe
# if you want a new instance, you will get the old one (already created) instance  

class Singleton:
    __instance = None # double underscore dile privet
    def __init__(self) -> None:
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('This is singleton. Already has an instance, use that one by calling get_instance method')
    
    @staticmethod # akhn r self deya lagbe na
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
    
first = Singleton.get_instance()
print(first)

second = Singleton.get_instance()
print(second) # akhn o exactly ager instance er reference e dicche

third = Singleton.get_instance()
print(third) # akhn o exactly ager instance er reference e dicche

Singleton() # not possible to call. because singleton e instance akbar e create hobe.