#Check if two sets are disjoint.							

Set_A = {1, 2, 3}
Set_B = {4, 5, 6}

if len(Set_A&Set_B) == 0:
    print("The Given Sets are Disjoint")
else:
    print(Set_A&Set_B)