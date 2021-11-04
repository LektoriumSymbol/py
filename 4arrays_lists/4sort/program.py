print("* * * This is your own sort method * * *")
print()

print("> This this the list")

list = [1, 20 ,30, 5, 8, 10, 21, 33, 50]

print(list)

n = len(list)

for i in range(n-1):
    for j in range(0, n-1):
        if list[j] > list[j + 1] :
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp

# for i in range(n-1):

#     for j in range(0, n-i-1):

#         if list[j] > list[j + 1] :
#             list[j], list[j + 1] = list[j + 1], list[j]

print("> This this the reversed list")

print(list)
