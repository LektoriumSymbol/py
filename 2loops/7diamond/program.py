print("* * * Diamond looks like this * * *")
print("Enter vertical count")
vertical = int(input())

horizontal_increment = 0
vertical_increment = 1
magic_increment = 0

meridian = int(vertical / 2)
meridian_counter = 0
magic = vertical_increment + meridian

while(vertical_increment <= vertical):
    horizontal_increment = vertical - magic
    while(horizontal_increment > 0):
        print("  ", end="")
        horizontal_increment -= 1

    horizontal_increment = 0
    while(horizontal_increment < vertical_increment + magic_increment):
        print("* ", end="")
        horizontal_increment += 1
    
    print()

    vertical_increment += 1

    if(meridian_counter < meridian):
        magic_increment += 1
        magic = vertical_increment + meridian
    else:
        magic_increment -= 3
        magic -= 1


    meridian_counter += 1
