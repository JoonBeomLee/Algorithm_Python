NOTATION = "012"

def convert_dec2sol(num):
    q, r = divmod(num, 3)
    
    # 기존 3진법 변경과 같지만 
    # 3으로 떨어지는 수만 4로 변경
    # [0, 1, 2] => [1, 2, 4]
    if r == 0: 
        n = '4'
        q = q - 1
        
    else: n = NOTATION[r]
    
    return convert_dec2sol(q) + n if q else n

def solution(n):
    answer = convert_dec2sol(n)
    
    return answer