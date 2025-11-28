#Check if two variables refer to the same object (use 'is').							
# "==" -> Checks Value Equality and "is" -> Checks Identity Equality
var1 = "Rama"
var2 = "Abhinav"
var3 = var1

if var1 is not var2:
    print("Variables 1 and 2  don't refer to same object")
if var3 is var1:
    print("Variables 1 and 3 refer to the same object ")
else:
    print("Variables dont refer to same object")