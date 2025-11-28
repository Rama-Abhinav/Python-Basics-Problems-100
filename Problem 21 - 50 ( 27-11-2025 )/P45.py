# Count digits in an integer.							

num = int(input("Enter Integer: "))

if num > 0:
    print(f"The No.of digits in the given integer {num} = {len(str(num))}")
elif num < 0:
    print(f"The No.of Digits in the given integer {num} = {(len(str(num)))-1}")
else:
    print(f"The No.of Digits in 0 = 1")
