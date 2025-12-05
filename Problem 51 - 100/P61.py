#Find the second largest number in a list.							

Num_List = [100,90,10,12]

Max1 , Max2 = float("-inf"), float("-inf")

for num in Num_List:
    if num > Max1:
        Max2 = Max1
        Max1 = num
    elif num > Max2 and num != Max1:
        Max2 = num

print(f"The Largest Number in the list is {Max1}\nThe Second Largest Number in the list is {Max2}")
