#Take marks of 5 subjects and print grade (A/B/C/D/F).							


m = input("Enter Marks in 5 subjects with spaces between them: ").split()
MARKS = [int(d) for d in m]

Avg = sum(MARKS)/5

if Avg >= 90:
    print("A+")
elif Avg >= 80:
    print("A")
elif Avg >= 70:
    print("B")
elif Avg >= 60:
    print("C")
else:
    print("Improve ")