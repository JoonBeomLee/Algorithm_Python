# 에라토스테네의 체
def isPrime_v02(num):
    if num <= 1: return False
    
    i = 2
    while i*i <= num:
        if num % i == 0: return False
        i += 1

    return True

while True:
    N = int(input())
    if N == 0: break
    
    count = 0
    for num in range(N+1, 2*N+1):
        if isPrime_v02(num): count+=1
            
    print(count)