#Invert a dictionary (keys become values and vice versa).							

dict1 = {
    "name": "Abhinav",
    "age": 18,
    "country": "India",
    "skills": "coding",
    "level": "beginner"
}

Swapped = {value:key for key, value in dict1.items()} #Dictionary Comprehensions

print(Swapped)