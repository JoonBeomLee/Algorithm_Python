def solution(num):
    answer = 0
    
    while True:
        if(num == 1): break
        if(answer == 500): answer = -1; break
                    
        # 짝수
        if num % 2 == 0:
            num = num / 2
            
        # 홀수
        elif num % 2 != 0:
            num = 3 * num + 1
            
        answer += 1
            
    return answer