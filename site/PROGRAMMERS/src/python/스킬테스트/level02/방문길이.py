import copy 

def solution(dirs):
    answer = 0
    cur_pos = [0, 0]
    visit = []
    #    상 하   좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    cnt = 1
    print("move pre : ", cur_pos)
    for d in dirs:
        x, y = cur_pos[0], cur_pos[1]
        
        if d == 'L':
            # 밖을 넘지 않는다면 이동
            if cur_pos[0] + dx[2] >= -5:
                mx = cur_pos[0] + dx[2]
                my = cur_pos[1] + dy[2]
            else: continue
            
        elif d == 'R':
            # 밖을 넘지 않는다면 이동
            if cur_pos[0] + dx[3] <= 5:
                mx = cur_pos[0] + dx[3]
                my = cur_pos[1] + dy[3]
            else: continue
                
        elif d == 'U':
            # 밖을 넘지 않는다면 이동
            if cur_pos[1] + dy[0] <= 5:
                mx = cur_pos[0] + dx[0]
                my = cur_pos[1] + dy[0]
            else: continue
                
        elif d == 'D':
            # 밖을 넘지 않는다면 이동
            if cur_pos[1] + dy[1] >= -5:
                mx = cur_pos[0] + dx[1]
                my = cur_pos[1] + dy[1]
            else: continue
        
        cur_pos[0] = mx
        cur_pos[1] = my       
        
        tmp_go = copy.copy([x, y, mx, my])
        tmp_back = copy.copy([mx, my, x, y])
        
        print(cnt, d, " move post : ", tmp_go)
        if tmp_go not in visit:
            visit.append(tmp_go)
            visit.append(tmp_back)
        
        tmp_pos = []
        cnt += 1
        
    print(visit)
    print(len(visit))
        
    return len(visit) // 2