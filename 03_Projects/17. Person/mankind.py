"""  
All about mankind
Purpose: Inheritance
"""

class Human:
    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height
        self.weight = weight

class Police(Human):
    def __init__(self, cases, nationality, gender, height, weight):
        # gender, height, weight
        super().__init__(gender, height, weight)
        self.cases = cases
        self.nationality = nationality

class CSEngineer(Human):
    def __init__(self, love_to_code, has_gf, gender, height, weight):
        super().__init__(gender, height, weight)


if __name__ == '__main__':
    # police = Police(True, 'Bangladeshi', 'male', 6, 70)
    # print(police.weight)
        
    engr = CSEngineer(True, False, 'male', 6, 70)
    print(engr.weight)

    engr2 = CSEngineer(height=80, has_gf=True, love_to_code=False, gender='female', weight=67)
    print(engr2.weight)