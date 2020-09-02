count = int(input())

for i in range(count):
    for j in range(count, i+1, -1):
        print(" ", end="")
        
    for k in range(i+1):
        print("*", end="")
        
    print("\n", end="")