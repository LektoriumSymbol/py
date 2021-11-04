print("* * * This is your own append method * * *")
print()

print("> This this the list")

list = [1,2,3]

print(list)

print("> Enter value to add:")
val = input("> ")

#arr.append(int(val))

result_list = [0] * (len(list) + 1)

index = 0

while(index < len(list)):
    result_list[index] = list[index]
    index += 1

result_list[index] = int(val)

print("> The result list is")

print(result_list)
