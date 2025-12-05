#Check if a key exists in dictionary.							

dict = {
    "name": "Abhinav",
    "age": 18,
    "country": "India",
    "skills": "coding",
    "level": "beginner"
}

Keys = dict.keys()
Key_Val = input("Enter the Key to Check: ")

if Key_Val in Keys:
    print(f"The Key Value __{Key_Val}__ Exists in the Dictionary")
else:
    print(f"The Key Value __{Key_Val}__ Does Not Exist in the Dictionary")