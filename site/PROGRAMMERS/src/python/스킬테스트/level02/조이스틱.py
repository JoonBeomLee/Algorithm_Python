def solution(name):
    idx, answer = 0, 0
    # 각 알파벳의 최소 이동 값
    name_pos = [min( ord(name_ch) - ord("A"), ord("Z") - ord(name_ch) + 1 ) for name_ch in name ]
    
    while True:
        # 현재 차래의 이동횟수를 ++
        answer += name_pos[idx]
        name_pos[idx] = 0   # 추가한 알파벳 -> 0
        
        # 전부 이동시 loop break
        if sum(name_pos) == 0: break
        
        # 왼, 오른 위치값
        l_idx, r_idx = 1, 1
        
        # 이동가능한 위치값 search
        while name_pos[idx - l_idx] == 0: l_idx += 1
        while name_pos[idx + r_idx] == 0: r_idx += 1 
        
        # 최적의 이동을 위해 
        # 이동이 짧은 곳을 이동
        answer += l_idx if l_idx < r_idx else r_idx
        idx += -l_idx if l_idx < r_idx else r_idx
            
    
    return answer