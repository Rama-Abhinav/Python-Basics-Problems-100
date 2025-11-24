#Check if a string is a palindrome.							

Word = input("Enter Word to Check: ")

if Word == ("".join(reversed(Word))): print("Given word is palindrome!!")
else: print("Given word is not palindrom")

