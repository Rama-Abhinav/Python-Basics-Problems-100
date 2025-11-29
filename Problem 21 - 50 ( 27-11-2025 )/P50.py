#Find LCM of two numbers using while loop.							

a, b = map(int, input("Enter Numbers a and b whose LCM is to be found: ").split()) #Map Syntax:- map(function to be applied on iterable , iterable)

lcm = max(a,b)

while True:
    if lcm%a == 0 and lcm%b == 0:
        print(f"LCM of {a} and {b} = {lcm}")
        break
    lcm+=1    

