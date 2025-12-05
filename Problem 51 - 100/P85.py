#Write a function to return factorial.							
import sys 
sys.set_int_max_str_digits(10000)
def Factorial(n):
    Fact = 1
    for i in range(1,n+1):
        Fact *= i
    print(Fact)    

Factorial(6)