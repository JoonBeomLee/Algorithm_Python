def isPrime(num):
    if num == 1: return False
    
    for i in range(2, num):
        if num % i == 0: 
            return False
    
    return True

T = int(input())
nums = list(map(int, input().split(" ")))
count = 0

for num in nums:
    if isPrime(num): 
        count += 1
        
print(count)