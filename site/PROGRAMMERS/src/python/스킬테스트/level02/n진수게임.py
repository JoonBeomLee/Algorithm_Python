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
    
    tmp = num_convert(8, 2)
    
    while True:
        if len(num_list) >= t: break
    
    print(num_list)
    
    return answer