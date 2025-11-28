#Check leap year.							

YEAR_input = input("Enter Year: ")
year = [int(d) for d in YEAR_input]
n=len(year)+1

for i in year[1:n]:
    if i != 0:
        if (int(YEAR_input) % 4) == 0:
            print("Given Year is a Leap Year")
            break
        else:
            print("Not A Leap Year!!!")
            break
else:      
    if (int(YEAR_input) % 100) == 0 and (int(YEAR_input) % 400) == 0:
        print("Year is a Leap Year")
    else:
        print("year is not a leap year")
