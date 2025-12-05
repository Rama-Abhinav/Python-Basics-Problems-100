#Convert list to tuple and tuple to list.							

Chars = input("Enter Charecters : ").split()
T_Chars = tuple(Chars)
print(f"Chars by default is in list converting list to tuple: {Chars} -----> {T_Chars}")
print(f"Converting Tuple to List: {T_Chars} ---> {list(T_Chars)}")

