print("* * * This is your calculator * * *")

while(True):
    print("> First input: ", end="")
    a = int(input())
    print("> Second input: ", end="")
    b = int(input())
    print("> Action: ", end="")
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
                    print("! Can't be devided by zero")
            case _:
                print("! Non reserved action")

    print("> Result is: %s" % result)
    print()