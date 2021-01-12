"""
def get_divisors(num):
    # 약수 구하기
    divisors = []
    t_num = int(num/2)

    divisors.append(num)
    while t_num >= 1:
        if num % t_num == 0 :
            divisors.append(t_num)
        t_num -= 1
        
    return divisors

def solution(brown, yellow):
    # 가로 >= 세로
    answer = []
    # tile 총 수
    total = brown + yellow 
    # 약수 list
    divisor_list = get_divisors(total)
    
    # yellow 약수 list
    yellow_div_list = get_divisors(yellow)
    
    print(divisor_list)
    print(yellow_div_list)
    
    # 약수 list 개수
    divisor_cnt = len(divisor_list)
    
    # 약수 중간 idx
    mid_idx = int(divisor_cnt / 2)
    
        # 홀수
    if divisor_cnt % 2 != 0:
        answer = [divisor_list[mid_idx], divisor_list[mid_idx]]
    # 짝수
    else: 
        answer = [divisor_list[mid_idx-1], divisor_list[mid_idx]]
        print("double :: ", answer)  
    
    return answer
"""

def solution(brown, yellow):
    # 1 ~ Yellow
    # yellow의 가로 세로 찾을 때 까지 회문
    for N in range(1, yellow+1):
        # 나누어 떨어지는 N이라면
        # N은 가로,세로 중 한쪽 길이
        if yellow % N == 0:
            # length 는 나머지 길이
            length = yellow // N 
            
            # N, length = yellow의 길이
            # yellow는 카펫의 가운데에 위치해야한다
            # 전체 카펫 길이는 N + 2, length + 2로
            # 전체 카펫의 넓이 - Yellow = brown 일 경우
            # yellow의 가로, 세로 길이 확인
            if (((N + 2) * (length + 2)) - (N * length)) == brown:
                # 그 중 가로의 길이가 항상 넓기에
                # 둘 중 큰 값이 가로
                # 둘 중 작은 값이 세로
                return [max(N + 2, length + 2), min(N + 2, length + 2)]