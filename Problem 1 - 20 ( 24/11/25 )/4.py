#Swap two variables without using a third variable.							

Var1 = int(input("Enter Variable 1: "))
Var2 = int(input("Enter Variable 2: "))


"""
#Swapping of Variable using third variable
Var3 = Var1
Var1 = Var2
Var2 = Var3

print(f"Var1 = {Var1} and Var2 = {Var2}")
"""

Var1 += Var2
Var2 = Var1 - Var2
Var1 -= Var2

print(f"Var1 = {Var1} and Var2 = {Var2}")

