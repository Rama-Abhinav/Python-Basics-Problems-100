# Write a function that takes variable arguments and returns their sum.							

def Variable(*nums):
    total = 0
    for i in nums:
        total += i
    return(total)

print(Variable(1,2,3,4,5))