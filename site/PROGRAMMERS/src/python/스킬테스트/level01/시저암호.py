def solution(s, n):
    answer = ''
    
    # chr()  |  ord()    
    for s_idx in s:
        tmp_int = ord(s_idx)
        
        # A - Z
        if tmp_int + n > 90 and tmp_int <= 90:
            tmp_int = 65 + ((tmp_int + n) - 91)
            
        # a - z    
        elif tmp_int + n > 122 and tmp_int <= 122:
            tmp_int = 97 + ((tmp_int + n) - 123)
            
        # space
        elif tmp_int == 32:
            tmp_int = 32
        
        else:
            tmp_int += n
            
            
        answer += chr(tmp_int)
        
    return answer