NUM = "0123456789ABCDEF"

def num_convert(num, n):
    result = ""
    
    q, r = divmod(num, n)
    if q == 0:
        return NUM[r]
    else:
        return num_convert(q, n) + NUM[r]

def solution(n, t, m, p):
    answer = ''
    num_list = []
    my_list = []
    
    num = 0
    man_idx = 0
    converted_num = "0"
    
    while True:
        if len(my_list) >= t: break
        
        num_list.extend(converted_num)
        
        for c_n in converted_num:           
            # 본인 차례
            if man_idx == p - 1:
                my_list.extend(c_n)
            
            man_idx += 1
            
            # 순서 초기화
            if man_idx == m:
                man_idx = 0
            
        num += 1
        converted_num = num_convert(num, n)
    
    my_list = my_list[:t]
    answer = ''.join(my_list)
    
    return answer