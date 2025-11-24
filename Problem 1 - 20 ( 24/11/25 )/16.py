#Convert the first letter of every word to uppercase (title case).							

Sentence = "Here are the best and most Pythonic ways to remove all spaces from a string — from most efficient to most readable."


#----xxx Removes words with punctuation xxx ----#
"""
Sentence_List = Sentence.split()
New_Sentence_List = []

for word in Sentence_List:
    if word.isalpha() == True:
        New_Sentence_List.append(word.capitalize())
    

print(" ".join(New_Sentence_List))
"""

print(Sentence.title())