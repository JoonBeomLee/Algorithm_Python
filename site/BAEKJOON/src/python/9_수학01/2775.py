# 재귀함수 .py에서는 시간 초과 
# 실행속도가 빠른 pypy로 구동
# h 층 (0층이 시작) 
# w 호 (1호가 시작)
def check_room(h, w):
    if w == 1:
        return 1
    elif h == 0:
        return w
    else:
        return check_room(h-1, w) + check_room(h, w-1)
    
T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    
    print(check_room(k, n))