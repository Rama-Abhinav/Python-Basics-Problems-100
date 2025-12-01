#Count even and odd numbers in a list						

print("To Display the No.of Odd and Even Numbers in a given range specify the start and stop ranges\n")
Start = int(input("Enter Starting Of Range: "))
End = int(input("Enter End of Range: "))

Num_List = list(range(Start, End+1))
Odd , Even = 0, 0
for num in Num_List:
    if num % 2 == 0:
        Even += 1
    elif num%2 != 0:
        Odd += 1

print(f"In the List having Numbers from {Start} to {End} the No.of\nOdd Numbers = {Odd}\nNo.of Even Numbers = {Even}\n")
