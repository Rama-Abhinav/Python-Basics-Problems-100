#Unpack a tuple into variables.							

Tuple = (1,2,3,4)
import string
Vars= list(string.ascii_lowercase[:4])

Zip_VarsTOVals = list(zip(Vars, Tuple))

for i in Zip_VarsTOVals:print(i)