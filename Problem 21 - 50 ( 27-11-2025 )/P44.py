#Multiplication table of a number selected by the user.							

Num = int(input("Enter Number to print its multiplication table: "))
Tab_till = int(input("Enter Number till which tabels are to be computed: "))


for i in range(0, Tab_till+1):
    print(f"{Num} x {i} = {Num*i}")