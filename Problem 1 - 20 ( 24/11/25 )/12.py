#Count vowels in a string.							

word = "pneumonoultramicroscopicsilicovolcanoconiosis "
vowel_count = 0

"""
for letter in word:
    for vowel in ["a","e","i","o","u"]:
        if letter == vowel:
            vowel_count += 1
        else: continue
"""
for letter in word:
    if letter in {"a","e","i","o","u"}:             #Set lookup method
        vowel_count += 1
    else: continue


print(vowel_count)
        