print("* * * This is your own reverse method * * *")
print()

print("> This this the list")

list = [1,2,3,5,8,10]

print(list)

list_reversed = [0] * len(list)
index = -1

for x in list:
    list_reversed[index] = x
    index -= 1

print("> This this the reversed list")

print(list_reversed)
