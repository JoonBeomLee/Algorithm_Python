# pypy3로 구동
# 에라토스테네의 체
def isPrime_v02(num):
    if num <= 1: return False
    
    i = 2
    while i*i <= num:
        if num % i == 0: return False
        i += 1

    return True

def search_goldbach(prime_list):
    gold_list = {}
    
    for prime01 in prime_list:
        for prime02 in prime_list:
            if prime01 + prime02 == N:
                gold_list[abs(prime01-prime02)] = f"{prime02} {prime01}"
    
    print(gold_list[min(gold_list.keys())])
        

T = int(input())

for _ in range(T):
    N = int(input())
    
    prime_list = []
    for n in range(N+1):
        if isPrime_v02(n):
            prime_list.append(n)
            
    search_goldbach(prime_list)