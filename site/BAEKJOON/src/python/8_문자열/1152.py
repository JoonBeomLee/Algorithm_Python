words = input().split(" ")

count = 0
for i in words:
    if( i == ""): count += 1

print(len(words) - count)