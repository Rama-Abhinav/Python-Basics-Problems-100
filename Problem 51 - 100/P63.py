#List comprehension: create a list of squares for numbers 1–20.							

Num_List = list(range(1,21))

Sq_List_Comp = [int(i**2) for i in Num_List ]

print(Sq_List_Comp)