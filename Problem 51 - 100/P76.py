#Merge two dictionaries.							

dict1 = {
    "name": "Abhinav",
    "age": 18,
    "country": "India",
    "skills": ["python", "video editing"],
    "level": "beginner"
}

dict2 = {
    "age": 19,
    "city": "Hyderabad",
    "skills": ["automation", "AI"],
    "status": "learning",
    "dream": "billionaire"
}
dict1.update(dict2)
print(f"Merged Dictinary is : {dict1}")