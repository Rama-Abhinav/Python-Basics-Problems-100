#Print all prime numbers from 1 to 100.							

from math import sqrt

for i in range(2,101):
    prime_check = True
    for j in range(2, int(sqrt(i))+1):
        if i%j == 0:
            prime_check = False
            break
    if prime_check:
            print(i,end=" ")
    