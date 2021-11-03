print("* * * This is your fibonacci * * *")

def fib(n):
    if(n <= 1): return n

    result = fib(n - 1) + fib(n - 2)
    
    return result

while(True):
    print("> Number in sequence to calculate: ", end="")
    n = int(input())

    print(fib(n), end=" ")
    print()

    
