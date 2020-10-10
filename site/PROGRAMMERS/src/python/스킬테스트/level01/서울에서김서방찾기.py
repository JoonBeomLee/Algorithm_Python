def solution(seoul):
    answer = 0
    
    for s_idx in range(len(seoul)):
        if seoul[s_idx] == "Kim":
            answer = f'김서방은 {s_idx}에 있다'
            break
            
    return answer