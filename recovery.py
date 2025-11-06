class student:
    def __init__(self, name:str, program:str, hostel:str, age:int, level:int):
        self.name = name
        self.program = program
        self.hostel = hostel
        self.age = age
        self.level = level
    
    def display_info(self):
        print(f'=====STUDENT DETAILS========\n'\
        f'Name: {self.name}\nProgram: {self.program}\nHostel: {self.hostel}\nAge: {self.age}\nCurrent Level: {self.level}')


Student1 = student("Lloyd Kwadwo Agyapong", "Information Systems and Technology(IS)", "The Point", 20, 300)
Student1.display_info()