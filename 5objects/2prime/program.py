print("* * * This is your prime number checker * * *")

class Checker:
    
    def is_prime(num):
        is_prime = False
        if num > 1:
            for i in range(2, int(num/2)+1):           
                if (num % i) == 0:
                    break
            else:
                is_prime = True

        return is_prime


while(True):
    print("> Type in your number to check : ", end="")
    x = int(input())

    print("> Is a prime number!" if Checker.is_prime(x) else "> Is a complex number!")
    print()