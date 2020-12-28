import itertools

def is_prime(num):
    mid = int(num ** 0.5)
    result = True
    
    if num <= 1:
        result = False
    
    for i in range(2, mid + 1):
        if num % i == 0:
            result = False
            break
            
    return result

def solution(numbers):
    answer = 0
    combis = []
    
    # 조합 자리수
    # 2 ~ len(numbers)
    for str_len in range(2, len(numbers) + 1):
        combis += list(set(map(''.join, itertools.permutations(numbers, str_len)))) # 3개의 원소로 순열 만들기
    
    
    # numbers 중복 제거
    set_numbers = list(set(numbers))
    # numbers로 만들어진 순열 + 중복제거 numbers
    combis = combis + set_numbers
    # str -> int
    combis = list(map(int, combis))
    prime_list = []
    
    for num in combis:
        if is_prime(num): 
            prime_list.append(num)
    prime_list = list(set(prime_list))
    
    return len(prime_list)