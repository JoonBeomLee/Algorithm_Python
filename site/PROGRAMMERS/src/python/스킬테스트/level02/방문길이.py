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
    visit.append(copy.copy(cur_pos))
    for d in dirs:
        if d == 'L':
            # 밖을 넘지 않는다면 이동
            if cur_pos[0] + dx[2] >= -5:
                cur_pos[0] += dx[2]
                cur_pos[1] += dy[2]
            else: continue
            
        elif d == 'R':
            # 밖을 넘지 않는다면 이동
            if cur_pos[0] + dx[3] <= 5:
                cur_pos[0] += dx[3]
                cur_pos[1] += dy[3]
            else: continue
                
        elif d == 'U':
            # 밖을 넘지 않는다면 이동
            if cur_pos[1] + dy[0] <= 5:
                cur_pos[0] += dx[0]
                cur_pos[1] += dy[0]
            else: continue
                
        elif d == 'D':
            # 밖을 넘지 않는다면 이동
            if cur_pos[1] + dy[1] >= -5:
                cur_pos[0] += dx[1]
                cur_pos[1] += dy[1]
            else: continue
        
        tmp_pos = copy.copy(cur_pos)
        tmp_pos.append(copy.copy(d))
        
        print(cnt, d, " move post : ", tmp_pos)
        if tmp_pos not in visit:
            visit.append(copy.copy(tmp_pos))
        
        tmp_pos = []
        cnt += 1
        
    print(visit)
    print(len(visit))
        
    return len(visit) - 1