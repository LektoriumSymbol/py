print("* * * This is your fibonacci set via loop * * *")

N = int(input("> Enter number of elements in Fibonacci Series, please, N : "))
a = 0
b = 1 
result = "0, 1, "

for i in range(0, N):
    temp = a + b

    result += str(temp) + ", "
    
    a = b
    b = temp

print("> Result set is: ")
print(result[0:-2])
