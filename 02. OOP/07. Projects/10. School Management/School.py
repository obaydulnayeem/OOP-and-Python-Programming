class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.classrooms = {} # composition

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def student_admission(self, student, classroom_name):
        if classroom_name in self.classrooms:
            # TODO: set student id (roll num) at the time of adding the student
            self.classrooms[classroom_name].add_student(student)
        else:
            print(f'No classroom as named{classroom_name}')