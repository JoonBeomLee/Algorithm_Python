import copy

global maps

def init_maps(rows, columns):
    global maps
    
    map_ = 1
    maps = []
    
    for r in range(rows):
        map_line = []
        for c in range(columns):
            map_line.append(map_)
            map_ += 1
            
        maps.append(map_line)
        
    return maps

def rotate_matrix_idx(st, ed):
    global maps
    
    row, col = len(maps), len(maps[0])
    
    change_stack = []
    value_stack = []
    
    up = []
    down = []
    right = []
    left = []
    
    # check
    for r in range(row):
        for c in range(col):
            val = maps[r][c]
            
            # 위-가로
            if r == st[0] and (st[1] <= c <= ed[1]):
                up.append([r, c, val])
                            
            # 우-세로
            if c == ed[1] and (st[0] < r <= ed[0]):
                right.append([r, c, val])
                
            # 아래-가로
            if r == ed[0] and (st[1] <= c < ed[1]):
                down.append([r, c, val])
                            
            # 좌-세로
            if c == st[1] and (st[0] < r < ed[0]):
                left.append([r, c, val])
                    
    down.reverse()
    left.reverse()
    
    change_stack.extend(up)
    change_stack.extend(right)
    change_stack.extend(down)
    change_stack.extend(left)
                
    return change_stack

def rotate_matrix(idx_list):
    global maps
    
    value_stack = []
    
    # idx -> 데이터 전환
    for stack in idx_list:
        value_stack.append(maps[stack[0]][stack[1]])
    
    # 1칸 전진
    value_stack.insert(0, value_stack.pop(-1))
    
    # 전진한 데이터 적용, 최소값 찾기
    min_value = value_stack[0]
    for stack in zip(idx_list, value_stack):        
        maps[stack[0][0]][stack[0][1]] = stack[1]
        
        if min_value > stack[1]:
            min_value = stack[1]
        
    return min_value
        

def solution(rows, columns, queries):
    answer = []
    
    maps = init_maps(rows, columns)
    
    for query in queries:
        st_pos = [query[0]-1, query[1]-1]
        ed_pos = [query[2]-1, query[3]-1]
        
        rotate_idxs = rotate_matrix_idx(st_pos, ed_pos)
        answer.append(rotate_matrix(rotate_idxs))
    
    return answer