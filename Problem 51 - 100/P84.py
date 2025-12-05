#Write a function to check if a number is prime.							
import math

def Prime_Check(Num):
    if Num<2:
        print("Not a Prime Number !!!")
    elif Num == 2:
        print("2 is a prime number (Only Even Prime Number)")
    elif Num > 2:
        for i in range(2, int(math.sqrt(Num))+1):
            if Num%i == 0:
                print("Number Not Prime !!!")
                break
        else:
            print(f"{Num} is prime number")


Prime_Check(1)
Prime_Check(2)
Prime_Check(13)
Prime_Check(15)