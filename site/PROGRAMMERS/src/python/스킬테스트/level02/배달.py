import math
from collections import deque

global G_K
global delivery_map
global min_dist
global visited

def search_dfs(N):
    global delivery_map
    # 경로
    path = deque()
    
    # 1번 노드 처음 이동
    path.append(N)
    # 시작노드의 이동거리는 0
    min_dist[N] = 0

    # 경로 회귀
    while path:
        # 방문한 node
        y = path.popleft()
        
        # 방문한 node에 연결된 node
        for x, node_list in enumerate(delivery_map[y]):
            
            # 연결된 경로가 있을경우
            if node_list != 0:
                
                # 경로를 통한 이동거리가 더 짧은 경우
                # 적용
                if min_dist[x] > min_dist[y] + delivery_map[y][x] and min_dist[y] + delivery_map[y][x] <= G_K:
                    min_dist[x] = min_dist[y] + delivery_map[y][x]
                    path.append(x)
            
    return 0

def solution(N, road, K):
    global delivery_map
    global min_dist
    global G_K
    
    G_K = K
    answer = 0
    delivery_map = [[0 for _ in range(N)] for _ in range(N)]
    min_dist = [math.inf for _ in range(N)]
    
    for r in road:
        # index 0부터 시작
        frm, to = r[0] - 1, r[1] - 1
        
        if delivery_map[frm][to] == 0 and delivery_map[to][frm] == 0:
            delivery_map[frm][to] = r[2]
            delivery_map[to][frm] = r[2]
        else:
                 
            if r[2] < delivery_map[frm][to]:
                delivery_map[frm][to], delivery_map[to][frm] = r[2], r[2]
        
    #print(delivery_map)
    start_node = 0
    search_dfs(start_node)
    
    answer = len([x for x in min_dist if x <= K])

    return answer