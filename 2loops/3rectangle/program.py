print("* * * Rectangle looks like this * * *")
print("Enter horizontal count")
horizontal = int(input())
print("Enter vertical count")
vertical = int(input())

horizontal_increment = 0
vertical_increment = 0

while(vertical_increment < vertical):
    horizontal_increment = 0
    
    while(horizontal_increment < horizontal):
        print("* ", end="")
        horizontal_increment += 1
    
    print()
    vertical_increment += 1
