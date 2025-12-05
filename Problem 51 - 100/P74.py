#Count frequency of words in a sentence.							

Sentence = (("""python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice python code learn repeat practice
""").lower()).split()
            
Unique_List_Of_Words = set(Sentence)
Freq_Dict = {}

for Word in Unique_List_Of_Words:Freq_Dict.update({Word:0})

Keys = Freq_Dict.keys()

for Word in Sentence:
    for Key in Keys:
            if Word == Key:
                Freq_Dict[Key] += 1

print("The Repeated Words in the Given Sentence Are:-")
for Freq in Freq_Dict.items():
     print(Freq)

