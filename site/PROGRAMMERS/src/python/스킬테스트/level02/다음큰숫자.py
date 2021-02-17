def dec2bin(num):
    one_count = 0
    
    while True:
        
        if num <= 0: break
            
        if num % 2 == 1: one_count += 1
        num = num // 2
    
    return one_count

def solution(n):
    answer = 0
    
    n_one_count = dec2bin(n)
    n += 1
    while True:
        if dec2bin(n) == n_one_count: 
            answer = n
            break
        
        n += 1
        
    return answer