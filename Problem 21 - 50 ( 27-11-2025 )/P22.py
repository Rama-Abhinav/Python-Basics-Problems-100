#Given 3 numbers, calculate the average.							
sum = 0
print("Enter Numbers: ")
for i in range(3):
    num = int(input())
    sum += num

print(f"Average = {sum/3}")
