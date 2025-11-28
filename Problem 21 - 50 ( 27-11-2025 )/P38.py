#Check if a number is prime.							

import math

num = int(input("Enter Number to Check: "))

if num < 2:
    print("Not Prime as Negative Numbers or 1 are not prime numbers")
elif num == 2:
    print("Only Even Prime Number is 2")
elif num > 2:
    for i in range(2,int(math.sqrt(num))):
        if num%i == 0:
            print("Not Prime Since Divisible by other numbers")
            break
    else:
        print("Given Number is a Prime Number")
            
