def solution(s):
    answer = True
    
    if len(s) not in [4, 6]: answer = False
    
    for s_idx in s:
        if not s_idx.isdigit(): answer = False 
    
    return answer