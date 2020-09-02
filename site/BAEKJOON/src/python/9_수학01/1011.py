import math

T = int(input())

for i in range(T):
    st, ed = map(int, input().split(" "))
    length = ed - st
    
    # 3 이하 거리 그대로
    if length <= 3: 
        print(length)
        continue
    
    N = int(math.sqrt(length))
    M = N + 1
    
    if length >= N * M + 1:
        print(N + M)
    elif length >= N ** 2 + 1:
        print(N*2)
    else:
        print(N * 2 - 1)