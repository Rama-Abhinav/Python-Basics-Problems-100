#Raise an exception if age < 18.							



try:
    Ask_Age = int(input("Enter Age in Number (1,2,18,34,etc.): "))
    if Ask_Age < 18:
        raise Exception("Your Age Should be More than 18")
    else:
        print("🤩🤩🤩 Congrats You Are A Major 🤩🤩🤩")
except Exception as e:
    print(f"Minor Alert 🫨 : {e} 🫨")