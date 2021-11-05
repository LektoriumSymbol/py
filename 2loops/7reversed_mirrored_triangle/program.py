print("* * * Reversed mirrored triangle looks like this * * *")
print("Enter vertical count")
vertical = int(input())

horizontal_increment = 0
vertical_increment = 0

while(vertical_increment < vertical):
    horizontal_increment = vertical_increment
    while(horizontal_increment > 0):
        print("  ", end="")
        horizontal_increment -= 1

    horizontal_increment = vertical - vertical_increment
    while(horizontal_increment > 0):
        print("* ", end="")
        horizontal_increment -= 1
    
    print()
    vertical_increment += 1
