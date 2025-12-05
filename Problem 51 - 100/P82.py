#Find the key with the smallest value.							

test_dict = {
    "apple": 45,
    "banana": 12,
    "orange": 67,
    "mango": 20,
    "kiwi": 9
}

Min = float("inf")

for Val in test_dict.values():
    if Val < Min:Min = Val

for Key, Value in test_dict.items():
    if Value == Min:print(f"\nThe Key with the smallest value is: _{Key}_ With a Value of {Value}\n")