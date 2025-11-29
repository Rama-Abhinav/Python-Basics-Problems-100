#Generate first N Fibonacci numbers.							

n = int(input("Enter no.of Fibonacci Series to be displayed: "))

fibo_list = [0]
Term = 1
Next_Term = 1

for i in range(n-1):
    fibo_list.append(Term)
    Term , Next_Term = Next_Term, Term + Next_Term  # Updating both term and next term at the sametime

print(fibo_list)
    
    
