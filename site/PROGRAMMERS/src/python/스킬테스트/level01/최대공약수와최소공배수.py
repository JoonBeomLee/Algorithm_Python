def UC_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def UC_lcm(x, y):
    result = (x * y) // UC_gcd(x, y)
    return result

def solution(n, m):
    answer = []
    
    answer.append(UC_gcd(n, m))
    answer.append(UC_lcm(n, m))
    return answer