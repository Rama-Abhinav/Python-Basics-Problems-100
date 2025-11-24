#Remove all spaces from a string.							

word_spaces = "ram   a   Abhi        nav c"
new_word = ""
for char in word_spaces:
    if char == " ":
        continue
    else:
        new_word += char

print(new_word)

# OR #

print(word_spaces.replace(" ",""))