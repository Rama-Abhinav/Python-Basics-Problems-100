#Print squares of list elements using a loop.							

import operator

print("To Display the Squares of Numbers in a given range specify the start and stop ranges\n")
Start = int(input("Enter Starting Of Range: "))
End = int(input("Enter End of Range: "))

Num_List = list(range(Start, End+1))

for i in Num_List:
    print(f"{i}^2 = {operator.pow(i,2)}")