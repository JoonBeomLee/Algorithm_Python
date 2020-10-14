def solution(n):
    answer = 0
    
    for n_idx in range(1, n+1):
        if n % n_idx == 0: answer += n_idx
    
    return answer