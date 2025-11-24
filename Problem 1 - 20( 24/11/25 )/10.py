#Take a sentence input and print how many characters it contains. 

Sen = input("Enter sentence:")
Char_Count = 0
for i in Sen:
    if i == " ": continue
    else: Char_Count +=1

print(Char_Count)
