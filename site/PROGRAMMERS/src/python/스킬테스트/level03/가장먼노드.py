from collections import deque

def solution(n, edge):
    answer = 0
    _map = {}
    visited = [False] * n
    
    # init map
    for e in edge:
        a = e[0]
        b = e[1]
        
        _map[a] = _map.get(a, []) + [b]
        _map[b] = _map.get(b, []) + [a]
        
    
    # init queue
    route = deque()
    route.append(1)
    visited[0] = 1
    
    while route:
        nodes = len(route)
        
        for n in range(nodes):
            current = route.popleft()
            
            for c in _map[current]:
                if visited[c - 1] == False:
                    visited[c - 1] = True
                    route.append(c)
    
    answer = nodes
    
    return answer