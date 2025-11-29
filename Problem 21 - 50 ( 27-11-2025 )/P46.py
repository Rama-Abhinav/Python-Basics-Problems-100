#Reverse a number using a loop.							

Num = input("Enter Number to be Reversed:")

for i in Num[::-1]:## Using slicing with a negative step
    print(i,end="")

print()

for i in reversed(Num):# Using the reversed method
    print(i, end="")