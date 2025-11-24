#Reverse a string without using slicing.							


def recursive_reverese(string):
    if len(string) == 0:
        return string
    else:
        return recursive_reverese(string[1:]) + string[0]

out = recursive_reverese("lamborgini")
print(out)

#OR#

print("".join(reversed("Abhinav")))