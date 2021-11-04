print("* * * This is your own binary search method * * *")
print()

def sort(list):

    n = len(list)

    for i in range(n-1):

        for j in range(0, n-i-1):

            if list[j] > list[j + 1] :
                list[j], list[j + 1] = list[j + 1], list[j]

    return list

def search(lst, target):
  min = 0
  max = len(lst)-1
  avg = (min+max)/2
  # uncomment next line for traces
  # print lst, target, avg  
  while (min < max):
    if (lst[avg] == target):
      return avg
    elif (lst[avg] < target):
      return avg + 1 + search(lst[avg+1:], target)
    else:
      return search(lst[:avg], target)

  # avg may be a partial offset so no need to print it here
  # print "The location of the number in the array is", avg 
  return avg

print("> This this the list")

array = [1, 20 ,30, 5, 8, 10, 21, 33, 50]

print(array)

sort(array)

print("> This this sorted list")

print(array)

value = int(input("> Enter a value to find it's position index in the list: "))

first = 0
last = len(array)-1
found = False

while first <= last and not found:
    pos = 0
    midpoint = (first + last)//2
    if array[midpoint] == value:
        pos = midpoint
        found = True
    else:
        if value < array[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1

print("......")

if found:
    print("> Value was found on the position with index: %s" % pos)
else:
    print("> Value was't found!")

print()



