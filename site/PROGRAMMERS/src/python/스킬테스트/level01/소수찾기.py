def solution(n):
    n = n+1
    answer = 0
    prime_arr = [True] * (n)
    
    # N의 최대 약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사 
    mid = int(n ** 0.5)
    for i in range(2, mid + 1):
        if prime_arr[i] == True:
            
            for j in range(i + i, n, i):
                prime_arr[j] = False
                
    answer = len([x for x in range(2, n) if prime_arr[x] == True])
    
    return answer