import sys      
sys.setrecursionlimit(10000) 

def fibonacci(num): 
    answer = 0 
    f0 = 0
    f1 = 1 
    
    if num<2: 
        return num
    else: 
        for i in range(1,num): 
            answer = f1 + f0 
            f0 = f1 
            f1 = answer
            
        return answer

def solution(n):
    if n >= 2: 
        answer = fibonacci(n) % 1234567
    else:
        answer = n
    return answer