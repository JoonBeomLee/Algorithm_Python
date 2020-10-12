def solution(n):
    answer = ''
    str_suback = ['수', '박']
    
    for idx in range(n):
        answer += str_suback[idx % 2]
    
    return answer