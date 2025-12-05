#Convert two lists into a dictionary.							

keys = ["Apple", "Banana", "Mango"]
values = [120, 40, 80]
Dict = {}

for key , value in zip(keys,values):
    Dict.update({key:value})
print(Dict)

print(dict(zip(keys,values)))  ## More Pythonic
