#Write a program for a simple calculator (+, -, *, /).							

op_input = str(input("Enter Operation to Perform(+,-,x,/): "))

def Addition():
    sum = 0
    print("Enter numbers and type 'EXIT' to stop':" )
    while True:
        user_input = input()
        if user_input.upper() == "EXIT":
            break
        else:
            sum += int(user_input)
    print(sum)

def Subtraction():
    diff = 0 
    print("Enter numbers and type 'EXIT' to stop':" )
    while True:
        user_input = input()
        if user_input.upper() == "EXIT":
            break
        else:
            diff -= int(user_input)
    print(diff)

def Multiplication():
    Product = 1
    print("Enter numbers and type 'EXIT' to stop:" )
    while True:
        user_input = input()
        if user_input.upper() == "EXIT":
            break
        else:
            Product *= int(user_input)
    print(Product)

def Division():
    print("Enter numbers and type 'EXIT' to stop:" )
    Num1 = float(input("Enter 1st Number: "))
    Q = Num1/1
    while True:
        user_input = input()
        if user_input.upper() == "EXIT":
            break
        else:
            Q /= float(user_input)
    print(Q)

        

match op_input:
    case "+":
        Addition()
    case "-":
        Subtraction()
    case "x":
        Multiplication()
    case "/":
        Division()
    case _:
        print("Invalid Input Try Again !!")

