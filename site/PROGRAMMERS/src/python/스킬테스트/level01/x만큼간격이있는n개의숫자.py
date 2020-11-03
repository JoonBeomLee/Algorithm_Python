def solution(x, n):
    if x == 0: return [0] * n
    
    stop = (x * n) + 1 if (x * n) >= 0  else (x * n) - 1       
    answer = [num for num in range(x, stop, x)]

    return answer