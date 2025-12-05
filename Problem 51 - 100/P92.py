# Append user-entered text to a file until user types “stop”.							

print("Type all your details. Type 'EXIT' to stop.")

with open(r"C:\Users\ramaa\Desktop\Python-Basics-Problems-100\Problem 51 - 100\UserP92.txt", "a") as f:
    while True:
        user_input = input()

        if user_input == "EXIT":
            break   # stop the loop cleanly

        f.write(user_input + "\n")   # add newline for each entry
    