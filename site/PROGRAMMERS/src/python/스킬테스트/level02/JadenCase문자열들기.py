def solution(strs):
    answer = ''
    blank = True
    
    strs = strs.lower()
     
    for c_idx, ch in enumerate(strs):
        if ch == ' ':
            blank = True
            
        if ch != ' ' and blank:
            blank = False
            # 첫글자 숫자 아닌 경우
            if not ch.isdigit():
                ch = chr( ord(ch) - 32 )
            # 숫자인 경우
            elif ch.isdigit(): 
                answer += ch
                continue
            else: ch = chr( ord(ch) - 32 )
                
                
        answer += ch
        
    return answer