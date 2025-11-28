#Menu Drive Program for math operations 

import operator

Ops = input("""
Enter the Operation to be performed:-
Addition -> A
Subtraction -> S
Multiplication -> M
Division -> D
Remainder -> R
""")

N1, N2 = input("Enter Numbers 1 and 2 to perform operations: ").split()

Num1, Num2 = int(N1), int(N2)

match (Ops):

    case "A":
        print(operator.add(Num1, Num2))
    
    case "S":
        print(operator.sub(Num1,Num2))
    
    case "M":
        print(operator.mul(Num1,Num2))
    
    case "D":
        print(operator.truediv(Num1,Num2))
    
    case "R":
        print(operator.mod(Num1, Num2))

    case _:
        print("Inavlid Operation Enterd!!")