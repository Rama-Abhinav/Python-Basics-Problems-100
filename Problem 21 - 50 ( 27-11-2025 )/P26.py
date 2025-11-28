#Write a program using membership operator to check if a letter is in a string.							

Word = str(input("Enter Word: ")).upper()
letter = str(input("Enter Letter to be found: ")).upper()

try:
    if letter in Word:
        print(f"\n{letter} found in {Word} at index {Word.index(letter)}\n")
    else:
         raise ValueError("Value Not Found !!")
except ValueError as e:
        print(f"Error: {e}")
