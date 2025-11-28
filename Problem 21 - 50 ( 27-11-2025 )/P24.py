#Compare two strings lexicographically.							

"""
Strings are considered lexicographically same if :-
1. They have the same length 
2. Every charecter at each corresponding position in both strings is identical
"""

# Charecter by Char Cmp

def lex_compare(w1 :str, w2: str) -> int:           #Type Notation/ Type Line Hint
    lw1 , lw2 = len(w1), len(w2)
    n = min(lw1, lw2)
    for i in range(n):                              # To Comapre till the shortest word
        if w1[i] < w2[i]:                           # Word 1 comes after Word 2 lexicographically
            return -1
        elif w1[i] > w2[i]:                         # Word 1 comes before Word 2 lexicographically
            return 1

    # If the strings match for compelte length of the shorter string
    if lw1 < lw2:                                   #Shorter Strings come first
        return -1
    elif lw1 > lw2:
        return 1
    else:
        return 0

word1, word2 = str(input("Enter word1 and word2 with spaces: ")).split()

Response = lex_compare(word1, word2)

if Response == -1:
    print(f"{word1} comes before {word2} ")
elif Response == 1:
    print(f"{word1} comes after {word2}")
else:
    print(f"{word1} and {word2} are the same")