#Check if a number is divisible by both 3 and 5.	

Num = input("Enter Number: ")

Num_List = [int(d) for d in Num]

#Divisiblity by 3 and 5
if (sum(Num_List)%3) == 0:
    if (Num_List[-1]) == 0 or 5:
        print(f"{Num} is Divisible by both 3 and 5")
    else:
        print("Num is Divisible by 3")

