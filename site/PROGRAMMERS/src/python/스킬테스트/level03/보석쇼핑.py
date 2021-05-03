import copy

def solution(gems):   
    seted_gems = list(set(gems))
    gems_pack = []
    pos_stack = []
    
    answer = [0, len(gems)-1]
    answer_len = len(gems) - 1
    
    st_pos = 0
    ed_pos = len(gems) - 1
    
    pos_stack.append([st_pos, ed_pos])
    gems_pack = set(gems)
    
    while pos_stack:
        # 확인할 위치
        target_pos = pos_stack.pop()
        gems_pack = set(gems[target_pos[0]:target_pos[1]+1])
        
        # 조건 충족할 경우
        if len(gems_pack) == len(seted_gems):           
            
            #print("check")
            #print(gems_pack)
            #print(seted_gems)
            #print(target_pos)
            #print("\n\n")
            
            # 최소값 찾기
            if answer_len > target_pos[1] - target_pos[0]:
                #print("debug :: ",target_pos)
                answer = [target_pos[0], target_pos[1]]
                answer_len = target_pos[1] - target_pos[0]
            
            # 전체 탐색할경우 stop
            if target_pos[0] + 1 > target_pos[1]: break
            
            # 앞에서 전진
            pos_stack.append([target_pos[0] + 1, target_pos[1]])
            # 뒤에서 후진
            pos_stack.append([target_pos[0], target_pos[1] - 1])
    
    answer = [answer[0]+1, answer[1]+1]
    
    return answer
