def solution(absolutes, signs):
    answer = 0
    
    for idx, val in enumerate(signs):
        if val:
            answer += absolutes[idx]
        else:
            answer -= absolutes[idx]
    
    return answer