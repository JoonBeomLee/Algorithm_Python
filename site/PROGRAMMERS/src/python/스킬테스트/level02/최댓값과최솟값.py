def solution(s):   
    int_s = list(map(int, s.split()))
    answer = f'{min(int_s)} {max(int_s)}'
    
    return answer