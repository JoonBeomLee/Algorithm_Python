import itertools

def solution(number, k):
    answer = ''
    num_len = len(number) - k
    
    sorted_number = list(set(map(''.join, itertools.combinations(number, num_len))))
    
    # 중복제거
    # str -> int 변환
    sorted_number = list(set(map(int, sorted_number)))
    # 가장 큰 수 반환
    answer = max(sorted_number)
    # 문자열 형태 변환
    answer = str(answer)
    
    return answer