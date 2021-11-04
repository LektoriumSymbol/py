print("* * * This is your own index method * * *")
print()

print("> This this the list")

list = [1,2,3,5,8,10]

print(list)

value = input("> Enter value to find index: ")

def index(list, value):
    index = -1

    for x in list:
        index += 1

        if x == value:
            return index

    return -1

index = index(list, int(value))

if index != -1:
    print("> Value was found on the position with index: " + str(index))
else: 
    print("> Value wasn't found in the list!")
