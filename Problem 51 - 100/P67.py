#Create a set and add/remove elements.							

NUM_SET = {"RAMA","ABC",123,"OHH!!",10.45}
print(f"Real Set = {NUM_SET}\n")
## Adding elements 
NUM_SET.add("NEW ELEMENT")
print(f"Set with Added Element = {NUM_SET}\n")

## Removing Elements
try:
    NUM_SET.remove("O")
except KeyError:
    print("Element 'O' Does Not Exit Thus Key error raised\n")
NUM_SET.discard("ABC")
print(f"Set with 'ABC' element removed = {NUM_SET}\n")
