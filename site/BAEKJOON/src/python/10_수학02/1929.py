# 에라토스테네의 체
def isPrime_v02(num):
    if num <= 1: return False
    
    i = 2
    while i*i <= num:
        if num % i == 0: return False
        i += 1

    return True

M, N = map(int, input().split(" "))

for num in range(M, N+1):
    if isPrime_v02(num): print(num)