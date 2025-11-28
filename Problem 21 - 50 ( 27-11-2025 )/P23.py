#Write a program that uses logical operators to check if a number is between 10 and 20.							

Num = int(input("Enter Number: "))

for i in range(10,21):
    if Num == i:
        print("Number In Range of 10 to 20")
        break
else:
    print("Number not in given range")


