# Create a “Calculator” class that performs +, -, *, / by taking 'n' numbers

from operator import *
from functools import reduce
class Calculator:

    def __init__(self,*numbers):
        self.numbers = numbers

    def Add(self):
        result = sum(self.numbers)
        print(f"Sum of {self.numbers} = {result}")
    
    def Subtract(self):
        result = reduce(sub, self.numbers)
        print(f"Difference of {self.numbers} = {result}")
        
    def Multiply(self):
        result = reduce(mul, self.numbers)
        print(f"Product of {self.numbers} = {result}")
        
    
    def Divide(self):
        result = reduce(truediv,self.numbers)
        print(f"Quotient of {self.numbers} = {result}")
        

OP1 = Calculator(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
OP1.Add()
OP1.Subtract()
OP1.Multiply()
OP1.Divide()
