print("* * * This is your factorial * * *")

def factorial(n):
    if(n == 1): return n

    return n * factorial(n - 1)

while(True):
    print("> Number to calculate: ", end="")
    n = int(input())

    print(factorial(n))
    print()

    
