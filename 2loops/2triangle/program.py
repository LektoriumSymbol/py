print("* * * Triangle looks like this * * *")
print("Enter vertical count")
vertical = int(input())

horizontal_increment = 0
vertical_increment = 1

while(vertical_increment <= vertical):
    horizontal_increment = 0
    
    while(horizontal_increment < vertical_increment):
        print("* ", end="")
        horizontal_increment += 1
    
    print()
    vertical_increment += 1
