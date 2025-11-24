#Check the data type of different variables.							

List = Name, Age_str, BodyWeight_str = input("enter Name Age BodyWeight: ").split()
Age = int(Age_str)
BodyWeight = float(BodyWeight_str)

for var in Name, Age, BodyWeight:
    print(f"Variable {var} is of the data type {type(var)}\n")

print(type(List))