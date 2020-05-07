count = int(input())

for i in range(count):
    num, strs = input().split(" ")
    strs = list(strs)
    
    for j in strs:
        for k in range(int(num)):
            print(j,end="")
    print()