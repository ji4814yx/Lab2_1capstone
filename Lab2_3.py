from dataclasses import dataclass
# class Student:  ## create Student class
#     def __init__(self, name, college_id, gpa):
#         self.name = name
#         self.college_id = college_id
#         self.gpa = float(gpa)
#
#
#     def  __str__(self):
#         return f'Name: {self.name}\nid: {self.college_id}\nGrade: {self.gpa}\n'

@dataclass   ## dataclass
class Student:  # Student Class
    name: str
    college_id: str
    gpa: float

    def __str__(self): # create method to return the attribute and their values
        return f'Name: {self.name}\nid: {self.college_id}\nGrade: {self.gpa}\n'


def main():  # definition of of the function to take the values of the attribute
    adade = Student('Adade', 'ab2137cc', 3.7)
    john = Student('John', 'cs3279bc', 2.3)
    robert = Student('Robert', 'wf2213cd', 2.8)

    print(adade)
    print(john)

main()  ## This to  the main to execute the code





