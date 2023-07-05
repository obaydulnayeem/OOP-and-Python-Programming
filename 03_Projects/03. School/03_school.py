# has an error. student's info is not showing

class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self) -> str: # representation 
        return f'Student with name: {self.name}, class: {self.current_class}, id: {self.id}'

class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher: {self.name}, Subject: {self.subject},'
    
class School:
      def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

      def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

      def enroll(self, name, fee):
          if fee < 6500:
              return 'not enough fee'
          else:
              id = len(self.students) + 1
              student = Student(name, 'C', id)
              self.students.append(Student)
              return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'
          
      def __repr__(self) -> str:
          print('Welcome to', self.name)
          print('-----OUR TEACHERS------')
          for teacher in self.teachers:
              print(teacher)

          print('---------OUR STUDENTS----------')
          for student in self.students:
              print(student)
          return 'ALL DONE FOR NOW'

# nayeem = Student('Obaydul Hasan Nayeem', 9, 1)
# sams = Teacher('Samsuddoha Sams', 'Programming', 4)

# print(nayeem)
# print(sams)

phitron = School('Phitron')
phitron.enroll('tanvir', 5299)
phitron.enroll('zahid', 8699)
phitron.enroll('anis', 90000)

phitron.add_teacher('Md. Irfan', 'Algo')
phitron.add_teacher('Dr. Manjur Ahmed', 'Architecture')
phitron.add_teacher('Sohely Jahan', 'Microprocessor')

print(phitron)