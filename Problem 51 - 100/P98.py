# Create a “Calculator” class that performs +, -, *, /.							

class Calculator:

    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def Add(self):
        print(f"{self.num1} + {self.num2} = {self.num1 + self.num2}")
        return
    
    def Subtract(self):
        print(f"{self.num1} - {self.num2} = {self.num1 - self.num2}")
        return
        
    def Multiply(self):
        print(f"{self.num1} x {self.num2} = {self.num1 * self.num2}")
        return
    
    def Divide(self):
        print(f"{self.num1} ÷ {self.num2} = {self.num1 / self.num2}")
        return

OP1 = Calculator(10,10)
OP1.Add()
OP1.Subtract()
OP1.Multiply()
OP1.Divide()