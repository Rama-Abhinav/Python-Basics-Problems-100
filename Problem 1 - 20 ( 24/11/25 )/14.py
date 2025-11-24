#Find the frequency of each character in a string							

word = "pneumonoultramicroscopicsilicovolcanoconiosis"

"""
Count_dict = {}


for letter in word:
    if letter in Count_dict.keys():
        continue
    else:
        Count_dict.update({letter : 0})

for letter in word:
    for Match in Count_dict.keys():
        if letter == Match:
            Count_dict[Match] += 1
        else:
            continue

for key, val in Count_dict.items():
    print(f"{key}:{val}")

"""

# More pythonic Approach

from collections import Counter

freq = Counter(word)

for char, count in freq.items():
    print(f"{char}:{count}")