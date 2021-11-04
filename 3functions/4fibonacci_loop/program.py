print("* * * This is your fibonacci set via loop with semantic sugar * * *")

N = int(input("> Enter number of elements in Fibonacci series, please, N : "))

def fib(n):
    a, b = 0, 1
    
    while a <= n:
        print(a, end=' ')
        a, b = b, a+b
    
    print()

fib(N)
