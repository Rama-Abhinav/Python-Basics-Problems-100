#Create a dictionary of squares for numbers 1–10.							

Nums = list(range(1,11))
SQ_D = {x:x**2 for x in Nums}
print(SQ_D)