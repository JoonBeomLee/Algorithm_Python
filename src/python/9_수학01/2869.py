up, down, height = map(int, input().split(" "))
day_count = 0
climb = 0

if (height - down) % (up - down) != 0:
    day_count = ((height - down) // (up - down)) + 1
else:
    day_count = ((height - down) // (up - down))
    
print(day_count)