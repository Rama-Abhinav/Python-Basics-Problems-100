#Print Triangle Patterns

n = int(input("Enter No.of Rows in Traingle: "))

## Pattern 1 — Left-Aligned Increasing Triangle
for i in range(1,n+1):
    print("*"*i,end=" ")
    print()

## Pattern 2 - Right-Aligned Triangle

for i in range(1,n+1):
    print((n-i)*" "+"*"*i,end=" ")
    print()

## Pattern 3 — Centered Pyramid
for i in range(1,n+1):
        print(" "*(n-i)+"*"*((2*i)-1),end="")
        print() 