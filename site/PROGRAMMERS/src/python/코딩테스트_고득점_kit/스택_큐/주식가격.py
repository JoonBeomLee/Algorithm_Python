def solution(prices):
    answer = []
    
    for price_idx in range(len(prices)):
        tmp_sum = 0
        
        for answer_idx in range(price_idx + 1, len(prices)):
            tmp_sum += 1 
            
            if prices[price_idx] > prices[answer_idx]: break 
                
        answer.append(tmp_sum)

    return answer