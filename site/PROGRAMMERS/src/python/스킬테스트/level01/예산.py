def solution(d, budget):
    answer = 0
    d_sum = 0
    d_idx = 0
    
    d_arr = sorted(d)
    
    while True:
        # 배열 인덱스 범위 초과 방지
        if d_idx > len(d_arr) - 1 : break
        
        d_sum += d_arr[d_idx]
        d_idx += 1
        answer += 1
        
        # 합계가 넘어갈경우
        if d_sum == budget: break
            
        elif d_sum > budget: 
            answer -= 1
            break
            
    return answer