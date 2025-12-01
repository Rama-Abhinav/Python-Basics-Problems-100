#Reverse a list without using reverse().							


List = [str(a) for a in "NAME OF STUDENT"]
New_List = []
for i in List[::-1]:
    New_List.append(i)
print(f"{List}\n{New_List}")