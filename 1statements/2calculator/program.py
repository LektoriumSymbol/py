print("* * * This is your calculator * * *")
print("First input: ")
a = int(input())
print("Second input: ")
b = int(input())
print("Action: ")
sign = input()
result = 0

match sign:
        case "+":
            result = a + b
        case "-":
            result = a - b
        case "*":
            result = a * b
        case "/":
            if(b != 0):
                result = a / b
            else:
                print("Can't be devided by zero")
        case _:
            print("Non reserved action")

print("Result is: %s" % result)