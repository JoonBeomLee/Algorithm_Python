import math 

def solution(n):
    answer = 0
    sqrt_n = math.sqrt(n)
    
    # 제곱근이 정수일 경우
    if sqrt_n % 1 == 0: answer = (sqrt_n + 1)**2
    else: answer = -1
    
    return answer