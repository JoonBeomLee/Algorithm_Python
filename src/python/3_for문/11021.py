count = int(input())

for i in range(count):
    a, b = input().split(" ")
    a = int(a); b = int(b)
    print("Case #%d: %d" %(i+1, a+b) )