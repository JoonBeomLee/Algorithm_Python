def remove_zero(num_str):
    result = ''
    zero_count = 0
    
    for num in num_str:
        if num == '1':
            result += num
        else:
            zero_count += 1
            
    return result, zero_count
    
    #return ''.join(list(map(lambda x: '' if x == '0' else '1', num_str)))

def dec2bin(num):
    result = ''
    
    while True:
        if num <= 0: break
            
        result += str(num % 2)
        num = num // 2
        
    return result[::-1]

def solution(s):
    answer = [0, 0]
    result = s
    count = 0
    
    while True:
        if result == '1': break
            
        removed_zero, zero_count = remove_zero(result)
        
        #print(removed_zero, zero_count)
        result = dec2bin(len(removed_zero))
        
        answer[0] += 1
        answer[1] += zero_count
    
        #print(answer)
    
    return answer