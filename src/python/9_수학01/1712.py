a, b, c = input().split(" ")
a = int(a); b = int(b); c = int(c)

count = 0
sum_a = a
sum_b = 0
judge = True

if(b >= c): judge = False; count = -1
else: count = a / (c - b) + 1

print("%1d" %count)