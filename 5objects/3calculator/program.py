print("* * * This is your calculator * * *")

class Calculator:
    
    def calculate(self, a, b, sign):
        result = 0

        match sign:
                case "+":
                    result = self.sum(a, b)
                case "-":
                    result = self.sub(a, b)
                case "*":
                    result = self.mul(a, b)
                case "/":
                    if(b != 0):
                        result = self.div(a, b)
                    else:
                        print("! Can't be devided by zero")
                case _:
                    print("! Non reserved action")

        print("> Result is: %s" % result)
        print()

    @staticmethod
    def sum(a, b):
    # def sum(self, a, b):
        return a + b

    @staticmethod
    def sub(a, b):
    # def sub(self, a, b):
        return a - b

    @staticmethod
    def mul(a, b):
    # def mul(self, a, b):
        return a * b

    @staticmethod
    def div(a , b):
    # def div(self, a , b):
        return a / b



while(True):
    print("> First input: ", end="")
    a = int(input())
    print("> Second input: ", end="")
    b = int(input())
    print("> Action: ", end="")
    sign = input()

    calculator = Calculator()
    calculator.calculate(a, b, sign) 