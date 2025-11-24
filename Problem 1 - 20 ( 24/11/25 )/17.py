#Replace every vowel in a string with “*”.							

Word = "pneumonoultramicroscopicsilicovolcanoconiosis"

for letter in Word:
    if letter in {'a','e','i','o','u'}:
        Word = Word.replace(letter,"*")

print(Word)