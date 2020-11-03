a, b = map(int, input().strip().split(' '))

for floor in range(b):
    for window in range(a):
        print("*", end="")
    print()