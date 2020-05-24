def isPrime(num):
    if num == 1: return False
     
    for i in range(2, num):
        if num % i == 0: 
            return False
    
    return True

st = int(input())
ed = int(input())
sum_prime = 0
list_prime = []

for num in range(st, ed+1):
    if isPrime(num): 
        sum_prime += num
        list_prime.append(num)
        
print("-1" if sum_prime == 0 else f"{sum_prime}\n{min(list_prime)}")