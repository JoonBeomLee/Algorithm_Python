def solution(n):
    answer = 0
    n = list(map(int, str(n)))
    n = sorted(n, reverse=True)
    n = list(map(str, n))
    
    answer = int(''.join(n))
    
    return answer