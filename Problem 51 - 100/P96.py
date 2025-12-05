#Create a class “Student” with name, age. Add a method to display info.							

class StudentRecord:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def display_info(self):
        print(f"The Name of the Student is {self.name} and Age is {self.age}")

S1 = StudentRecord("Rama Abhinav C", 18)
S1.display_info()


