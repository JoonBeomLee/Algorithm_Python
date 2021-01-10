# input N
N = int(input())
# start posistion
X, Y = 1, 1

# input plans
plans = input().split()

# L, R, U, D (좌, 우, 상, 하)
move_dir = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 이동 계획 확인
for plan in plans:
    # L, R, U, D 반복하여
    # 현재 이동 계획으로 이동
    for i in range(len(move_dir)):
        if plan == move_dir[i]:
            nx = X + dx[i]
            ny = Y + dy[i]

    # 맵 벗어나는 경우 이동 무시
    if nx < 1 or ny < 1 or nx > N or ny > N: continue

    # 올바른 이동일 경우
    # 위치 적용
    X, Y = nx, ny

# 계획 완료 후 위치
print(X, Y)