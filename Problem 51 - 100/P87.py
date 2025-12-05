# Write a function to calculate nCr (combinations).							

from math import factorial
def Combination(n,r):
    
    print("\n=================  COMBINATION FORMULA  =================")
    print("                  n! ")
    print("         nCr = ---------")
    print("               r! (n - r)!")
    print("==========================================================\n")

    if n>=r and 0<=r<=n:
        result = factorial(n)/(factorial(r)*(factorial(n-r)))
        print(f"The No.of Ways to Choose {r} items from a set of {n} = {result} ways")
    else:
        print("Invalid n and r values")
    
n = int(input("The total number of items in the set: "))  
r = int(input("The number of items to choose from the set: "))
print("\n\n")
Combination(n,r)