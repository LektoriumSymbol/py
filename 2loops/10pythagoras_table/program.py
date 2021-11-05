print("* * * Pythagoras table looks like this * * *")
print("Enter horizontal start value")
h_start = int(input())
print("Enter horizontal end value")
h_end = int(input())
print("Enter vertical start value")
v_start = int(input())
print("Enter vertical end value")
v_end = int(input())

print()

spaces = v_end
while(spaces >= 1):
    print(" ", end="")
    spaces /= 10

print("|", end="")

max = h_end * v_end
max_count = 0

while(max > 1):
    max_count += 1
    max /= 10

start = h_start
while(start <= h_end):
    print(" ", end = "")

    spaces_count = 0
    spaces = start

    while(spaces >= 1):
        spaces_count += 1
        spaces /= 10

    spaces_count = max_count - spaces_count
    while(spaces_count >= 0):
        print(" ", end="") 
        spaces_count -= 1
    
    print(start, end="")
    start += 1

print()

spaces = v_end
while(spaces >= 1):
    print("-", end="")
    spaces /= 10

print("+", end="")

start = h_start
while(start <= h_end):
    print("-", end = "")

    spaces_count = 0
    spaces = start
    while(spaces >= 1):
        spaces_count += 1
        spaces /= 10

    spaces_count = max_count - spaces_count
    while(spaces_count >= 0):
        print("-", end="") 
        spaces_count -= 1
    
    spaces = start
    while(spaces >= 1):
        print("-", end="") 
        spaces /= 10
    
    start += 1
    
print()

while(v_start <= v_end):
    spaces_count = 1
    end = v_end
    while(end >= 1):
        spaces_count += 1
        end /= 10

    start = v_start
    while(start >= 1):
        spaces_count -= 1
        start /= 10

    while(spaces_count > 1):
        print(" ", end="") 
        spaces_count -= 1
    
    print(v_start, end="")    
    print("|", end="")

    start = h_start
    while(start <= h_end):
        print(" ", end = "")

        result = v_start * start
        spaces_count = 0
        while(result >= 1):
            spaces_count += 1
            result /= 10

        spaces_count = max_count - spaces_count
        while(spaces_count >= 0):
            print(" ", end="") 
            spaces_count -= 1
        
        result = v_start * start

        print(result, end="") 
        start += 1
    
    v_start += 1

    print()

print()