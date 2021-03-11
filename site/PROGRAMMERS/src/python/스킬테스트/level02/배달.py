global delivery_map
global min_dist

def search_dfs(st_node):
    visited = []
    
    stack = [st_node]
    visited = []
    
    while stack:
        v = stack.pop()
        
        for node in delivery_map[v-1]:
            if node != 0: stack.append(node)

def solution(N, road, K):
    global delivery_map
    global min_dist
    
    answer = 0
    delivery_map = [[0 for _ in range(N)] for _ in range(N)]
    min_dist = [0 for _ in range(N)]
    
    for r in road:
        delivery_map[r[0] - 1][r[1] - 1] = r[2]
        
    print(delivery_map)

    return answer