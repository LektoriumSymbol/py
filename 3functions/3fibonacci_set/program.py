print("* * * This is your fibonacci set * * *")

def fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return fibonacci(n-1) + fibonacci(n-2)

nterms = int(input("> How many terms? > "))  

print("> Fibonacci sequence:")  

for i in range(nterms):  
    print(fibonacci(i), end=" ")  

print()