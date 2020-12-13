def solution(numbers):
    numbers = list(map(str, numbers))
    # *3 의 이유
    # numbers의 인수 값인 num이 1000이하의 수이므로 
    # 같은 비교를 위해 3자리 수로 맞춘뒤 비교 위함
    numbers.sort(key = lambda num : num * 3, reverse = True)
    
    return str(int(''.join(numbers)))