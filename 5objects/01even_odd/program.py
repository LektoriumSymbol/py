print("* * * This is your even odd checker * * *")

class Checker:
    
    def get_result(x):
        return "Even" if x % 2 == 0 else "Odd"


while(True):
    print("> Type in your number to check : ", end="")
    x = int(input())

    result = Checker.get_result(x) 

    print(result)
    print()