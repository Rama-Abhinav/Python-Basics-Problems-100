#Find the greatest of 3 numbers.							

num_str = input("Enter Num1 Num2 and Num3: ").split()
num_list = [int(d) for d in num_str]
max = 0
for num in num_list:
    if num >max:
        max = num
    else:
        continue
print(f"Among to numbers {num_list} the maximum number is {max}")
