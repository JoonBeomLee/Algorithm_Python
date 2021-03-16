import copy
import math

def solution(n,a,b):
    answer = 1
    # 최대 토너먼트 경기수
    count_max = int(math.log(n, 2))
    # player list
    player = ['0' for _ in range(n)]
    player[a-1] = "A"
    player[b-1] = "B"
    
    tmp = copy.copy(player)
    while True:
        # 마지막 경기인 경우 stop
        if answer == count_max: break
        
        tmp_str = ''.join(tmp)
        
        # 두선수 붙어있을 경우 stop
        if tmp_str.find("AB") != -1:
            # 추가 판별
            # 경계로 붙어 있는 경우 토너먼트 1회 추가수행 필요
            if tmp_str.find("A")+1 == len(tmp) // 2:
                pass
            # 붙어는 있지만 경기가 다른 경우
            elif (tmp_str.find("B") + 1) % 2 != 0: 
                pass
            # 아닌 경우 stop - success
            else: break
                
        if tmp_str.find("BA") != -1: 
            # 추가 판별
            # 경계로 붙어 있는 경우 토너먼트 1회 추가수행 필요
            if tmp_str.find("B") + 1 == len(tmp) // 2:
                pass
            # 붙어는 있지만 경기가 다른 경우
            elif (tmp_str.find("A") + 1) % 2 != 0: 
                pass
            # 아닌 경우 stop - success
            else: break
        
        # 1회 토너먼트 진행
        # 대진표 조정
        p_idx = 0
        tmp = []
        while True:
            if p_idx % 2 == 1: continue
            
            # 1회 수행 할 경우 정지
            if len(tmp) == len(player) // 2: break
            
            # 오른쪽 player에 타겟이 있을 경우
            # 오른쪽이 올라감
            if player[p_idx + 1] in ["A", "B"]:
                tmp.append(player[p_idx+1])
                p_idx += 2
            # 아닌경우 왼쪽 player 올라감
            else:
                tmp.append(player[p_idx])
                p_idx += 2
        
        # deep copy
        player = copy.copy(tmp)
        answer += 1
    
    
    return answer