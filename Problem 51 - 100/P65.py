#Find frequency of elements in a tuple.							

user_in = tuple(input("Enter the Values: ").split())
Uq_Set = set(user_in)
Freq_Dictionary = {}
for Element in Uq_Set:Freq_Dictionary.update({Element:0})
for element in user_in:
    for key in Freq_Dictionary.keys(): 
        if element == key : Freq_Dictionary[key] +=1
for i in Freq_Dictionary.items(): print(i)
