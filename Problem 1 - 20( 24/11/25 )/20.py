#Find the longest word in a sentence.							

Sentence = "Here are the best and most Pythonic ways to remove all spaces from a string — from most efficient to most readable."
Sentence_List = Sentence.split()
Max_Len_word = ""
for word in Sentence_List:
    if word.isalpha() == True:
        if len(word) > len(Max_Len_word):
            Max_Len_word = word
        else:
            continue
    else:
        continue

print(Max_Len_word)
