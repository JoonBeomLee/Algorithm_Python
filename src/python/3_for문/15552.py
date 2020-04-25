import sys

count = int(input())

for i in range(count):
    n1, n2 = map(int, sys.stdin.readline().split())
    
    print(n1 + n2)