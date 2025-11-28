#Simple password validation (length > 6, contains number).							

import re

Password = input("Enter Passowrd (Should have more than 6 charecters and a min of one number): ")

if len(Password) > 6:
    if len(re.findall("[0-9]",Password)) >= 1:
        print("🤩🤩🤩🤩 Passoword Entered is Valid 🤩🤩🤩🤩")
else:
    print("Passowrd Invalid 🤬 as no.of charecters less than 6 🥴")


