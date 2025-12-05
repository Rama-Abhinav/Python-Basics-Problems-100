#Count vowels using a set.							

WORD = "helloworld"

V_C = 0 
for letter in WORD:
    for vowel in {"a","e","i","o","u"}:
            if letter == vowel:
                V_C += 1

print(V_C)

