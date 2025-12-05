#Read a file and print the longest line.							

with open(r"C:\Users\ramaa\Desktop\Python-Basics-Problems-100\Problem 51 - 100\P91Longestline.txt",'a') as f:
    f.write("""
1.Iron Man soared above the battlefield with blazing thrusters.
2.Thor summoned lightning that cracked across the sky.
3.Black Widow moved swiftly, striking with silent precision.
4.Hulk roared.
5.Doctor Strange opened a massive, swirling portal of shimmering golden energy that illuminated the entire city as the Avengers charged forward.
""")
    
with open(r"C:\Users\ramaa\Desktop\Python-Basics-Problems-100\Problem 51 - 100\P91Longestline.txt") as f:
    lines = f.readlines()
    longest_line = max(lines, key=len)
    print(longest_line)