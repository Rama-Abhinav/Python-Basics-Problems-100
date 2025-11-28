#Sum of numbers from 1 to N.							

Sum_Till = int(input("🤑 Enter Number(N) till which sum is to computed from 1: "))

sum = 0

for i in range(1,Sum_Till+1):
    sum += i

print(sum)