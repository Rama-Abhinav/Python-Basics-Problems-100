#Find max and min in a list without using built-in functions.							

num  = [10 ,20, 100, 1]

Max = 0 
Min = 0

for i in num:
    if i>Max:
        Max = i
    elif Max > i:
        Min = i

print(f"The Min and Max Value from the list {num} are {Min} and {Max}")