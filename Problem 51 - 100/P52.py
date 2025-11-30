#Count how many times a character appears in string (using loop).							

Word = input("Enter Word: ")
Char = input("Enter Charecter Whose Occurance is to be counted: ")
Occurance = 0
for Letter in Word:
    if Letter == Char:
        Occurance +=1
print(Occurance)