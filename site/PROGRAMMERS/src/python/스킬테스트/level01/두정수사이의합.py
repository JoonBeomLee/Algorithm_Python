def solution(a, b):
    answer = 0
    
    if a > b:
        tmp = a
        a = b
        b = tmp
    
    for num in range(a, b+1):
        answer += num
        
    return answer