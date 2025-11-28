#Check if a character is alphabet, digit, or symbol.							


import re

char = input("Enter Charecter: ")

alphabet = re.findall("[a-zA-Z]",char)
digit = re.findall("[0-9]",char)

if alphabet:
    print("Entered Charecter is an alphabet !!")
elif digit:
    print("Entered Charecter is a digit")
else:
    print("Entered charecter is a symbol")