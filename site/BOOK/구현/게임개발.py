# N, M 입력
N, M = map(int, input().split())

# 반문롹인 위한 map
# 0 방문 x
# 1 방문 o
visit = [[0] * M for _ in range(N)]

# 현재 위치, 방향 입력
x, y, direction = map(int, input().split())
# 현재 위치 방문 처리
visit[x][y] = 1

# 전체 맵정보 입력
# 바다 1
# 육지 0
_map = []
for i in range(N):
    _map.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    # 전역변수
    global direction
    direction -= 1

    if direction == -1:
        direction = 3

# solution 시작
count = 0
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    # 방문 x and 육지 -> 이동
    if visit[nx][ny] == 0 and _map[nx][ny] == 0:
        # 방문 처리
        visit[nx][ny] = 1
        x = nx
        y = ny
        # 이동
        count += 1
        # 회전횟수 초기화
        turn_time = 0
        
        continue

    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    # 방향 전환
    else:
        turn_time += 1

    # 네 방향 모두 이동 불가의 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        
        # 뒤로 이동 가능하다면 이동
        if _map[nx][ny] == 0:
            x = nx
            y = ny
        
        # 뒤가 바다로 막혀있는 경우
        else: 
            break

        turn_time = 0

# 정답 출력
print(count)