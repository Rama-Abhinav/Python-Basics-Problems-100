#Sum of all elements in a list.							

nums = input("Enter Numbers whose list will be created and sum will be generated: ").split()

nums_list = [int(d) for d in nums]

print(f"The list is {nums_list} and its sum is {sum(nums_list)}")