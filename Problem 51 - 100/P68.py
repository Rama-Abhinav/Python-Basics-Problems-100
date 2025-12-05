#Find union and intersection of two sets.							

Set_1 = {1,2,3,4,5,6,7} 
Set_2 = {5,6,7,8,9,10,11,12,13,14,15,16,17}

print(f"Union of {Set_1} and {Set_2} = {Set_1|Set_2}\n") # Union Operator "|" or Set_1.union(Set_2)

print(f"\nIntersection of {Set_1} and {Set_2} = {Set_1 & Set_2}\n") # Intersection Operator "&" or Set_1.intersection(Set_2)

print(f"\nDifference of {Set_2} and {Set_1} = {Set_2 - Set_1}\n") # Difference Operator "-" or Set_1.difference(Set_2)

print(f"\nSymmetric Difference between {Set_1} and {Set_2} = {Set_1 ^ Set_2}\n") # Symmetric Difference Operator "^" or Set_1.symmetric_difference(Set_2)


