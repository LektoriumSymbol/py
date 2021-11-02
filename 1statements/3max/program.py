print("* * * This is your max finder * * *")
print("First input: ")
a = int(input())
print("Second input: ")
b = int(input())
print("Third input: ")
c = int(input())
print("Fourth input: ")
d = int(input())
print("Fifth input: ")
e = int(input())

max = a

if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d
if max < e:
    max = e

print("Max value is: " + str(max))