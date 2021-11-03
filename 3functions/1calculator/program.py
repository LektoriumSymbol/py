print("* * * This is your calculator * * *")

def sum(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def calculator(a,b,sign):
    result = 0

    match sign:
            case "+":
                result = sum(a,b)
            case "-":
                result = sub(a,b)
            case "*":
                result = mul(a,b)
            case "/":
                if(b != 0):
                    result = div(a,b)
                else:
                    print("! Can't be devided by zero")
            case _:
                print("! Non reserved action")

    print("> Result is: %s" % result)
    print()

while(True):
    print("> First input: ", end="")
    a = int(input())
    print("> Second input: ", end="")
    b = int(input())
    print("> Action: ", end="")
    sign = input()

    calculator(a,b,sign)

    
