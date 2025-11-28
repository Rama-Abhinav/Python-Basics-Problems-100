#Factorial of a number.							

fn = int(input("Enter Number whose factorial is to be found: "))

if fn < 0: print("Factorial of negative numbers cannot be found !!")

elif fn == 0: print("0! = 1")

else:
    fact = 1
    for i in range(1,fn+1):
        fact *= i
    print(fact)