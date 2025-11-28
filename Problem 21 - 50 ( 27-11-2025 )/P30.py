#Compute the area of a triangle



print("Enter Triangle Details:-")
base, height = (input("Enter Base Length and Height of Triangle: ")).split()
base = int(base)
height = int(height)

Area = (0.5*base*height)
print(f"Area of triangle = {Area}sq.units")


