import random

class Person:
    def __init__(self, name) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def teach(self):
        pass

    def __repr__(self) -> str:
        return f'{self.name}'

    def evaluate_exam(self):
        marks = random.randint(0, 100)
        return marks
    
class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None

    def calculate_final_grade(self):
        for grade in self.subject_grade.values():
            print(self.name, grade)

    @property # setter
    def id(self):
        return self.__id
    
    @id.setter # getter
    def id(self, value):
        self.__id == value