def solution(s):
    answer = True
    p_count = 0
    y_count = 0
    
    s = s.lower()
    
    for s_idx in s:
        if s_idx == "p": p_count += 1
        elif s_idx == "y": y_count += 1
            
    if p_count != y_count: answer = False
    

    return answer