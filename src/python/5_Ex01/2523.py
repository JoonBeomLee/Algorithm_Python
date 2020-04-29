star_cnt = int(input())

for i in range(1, star_cnt*2):
    if i <= star_cnt:
        for j in range(i):
            print("*", end="")
    else:
        for j in range(i, star_cnt*2):
            print("*", end="")
            
    print()