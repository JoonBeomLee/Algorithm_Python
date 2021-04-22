def solution(list_a, list_b):
    answer = 0
    
    for idx, a in enumerate(list_a):
        answer += a * list_b[idx]
    
    return answer