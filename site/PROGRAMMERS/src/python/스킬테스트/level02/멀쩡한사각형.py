def UC_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def solution(w,h):
    answer = 1
    origin_wh = w * h
    gcd_wh = UC_gcd(w, h)
    
    answer = origin_wh - (w + h - gcd_wh)
    return answer