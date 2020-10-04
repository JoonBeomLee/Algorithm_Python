def solution(arr, divisor):
    answer = []
    
    for a_num in arr:
        if a_num % divisor == 0: answer.append(a_num)
        
    if(len(answer) == 0): answer.append(-1)
    answer.sort()
    
    return answer