#Print all keys and values line by line.							

dict = {
    "name": "Abhinav",
    "age": 18,
    "country": "India",
    "skills": "coding",
    "level": "beginner"
}
print("\t\t\t Key\t\t\t\t\t\t Value\t\t\t")
for Key, Value in dict.items():
    print(f"\t\t\t{Key}\t\t\t-->\t\t\t{Value}\t\t\t")