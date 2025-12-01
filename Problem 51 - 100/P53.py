#Remove duplicates from a string (keep first occurrences).							

Word = input("Enter The Words to Filter Duplicates: ")
Word_set = set([str(a) for a in Word])

for item in Word_set:print(item,end=" ")

