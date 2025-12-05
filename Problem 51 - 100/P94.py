# Handle invalid input for integer conversion.							

try:
    user = int(input("Enter an Integer: "))
except ValueError:
    print("Entered Value is Invalid Integer Type")