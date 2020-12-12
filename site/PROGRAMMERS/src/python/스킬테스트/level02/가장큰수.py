from itertools import permutations

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = list(permutations(numbers, len(numbers)))
    numbers = list(map(lambda num: ''.join(num), numbers)) 
    numbers = list(map(int, numbers))
    
    return str(max(numbers))