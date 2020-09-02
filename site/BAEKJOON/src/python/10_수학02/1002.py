import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split(" ")))
    
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    # 원이 겹칠경우
    if dist == 0:
        # 반지름이 같을 경우
        if r1 == r2: print(-1)
        else: print(0)
    
    # 겹치지 않을 경우
    elif dist > r1 + r2: print(0)
    # 한점이 겹칠 경우
    elif dist == r1 + r2: print(1)
    # 두점이 겹칠 경우
    elif dist < r1 + r2: 
        if r1 < r2 and r1 + dist == r2: print(1)
        elif r2 < r1 and r2 + dist == r1: print(1)
              
        elif r1 < r2 and r1 + dist < r2: print(0)
        elif r2 < r1 and r2 + dist < r1: print(0)
        else: print(2)

# 참조 : https://www.youtube.com/watch?v=Y0mJyV0KVdw