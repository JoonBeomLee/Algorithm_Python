def solution(prices):
    answer = []

    for price_idx in range(len(prices)):
        tmp_sum = 0
        tg_price = prices[price_idx]
        
        for answer_idx in range(price_idx+1, len(prices)):
            tmp_sum += 1
            if tg_price <= prices[answer_idx]: continue
            else: break
                
        answer.append(tmp_sum)
        
    return answer