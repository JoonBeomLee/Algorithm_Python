from collections import deque

# N, M을 공백으로 구분하여 입력
N, M = map(int, input().split())

# maze 미로 입력
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

# 4방향 정의 [상, 하, 좌, 우]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
# BFS = 최단거리 알고리즘에 최적화
def DFS(x, y):
    # BFS 위한 queue 라이브러리
    queue = deque()
    queue.append((x, y))

    # 큐가 빌때 까지
    while queue:
        x, y = queue.popleft()

        # 현재 노드에서 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 벗어 날 경우
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 벽 무시
            if maze[nx][ny] == 0: continue

            # 해당 노드 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1:
                # 전 이동거리에서 + 1
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    # 도착지 까지 최단 거리 반환
    return maze[N - 1][M - 1]

# BFS
# maze 최단 탈출 거리 출력
print(DFS(0, 0))