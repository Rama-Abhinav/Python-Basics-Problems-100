# Check if a substring exists inside a string (without using in).							

word = "pneumonoultramicroscopicsilicovolcanoconiosis"

sub = "ramicro"

check = word.find(sub)

if check  != -1:
    print("Substring exists")

else:
    print("Substring doesn't exist")