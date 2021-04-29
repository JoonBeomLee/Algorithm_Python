from collections import deque

#   상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0] 

global n, m
global g_map

# BFS 소스코드
def bfs(x, y):
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for di in range(4):
            nx = x + dx[di]
            ny = y + dy[di]
            
            # 맵 탈출 방지
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            # 벽 무시
            if g_map[nx][ny] == 0: continue
                
            # 노드 첫방문시 최단거리 기록
            if g_map[nx][ny] == 1:
                g_map[nx][ny] = g_map[x][y] + 1
                queue.append((nx, ny))
                
    return g_map[n-1][m-1]

def solution(maps):
    global n, m, g_map
    
    g_map = maps
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    # 길찾기 함수 호출
    answer = bfs(0, 0)
    
    if answer == 1:
        answer = -1
    
    return answer