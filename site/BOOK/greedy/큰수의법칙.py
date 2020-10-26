
# my code start

# N 2행에 입력될 배열의 크기
# M 숫자가 더해지는 횟수
# K 선택된 숫자가 연속으로 더해질수 있는 횟수
N, M, K = map(int, list(input().split()))
num_arr = list( map(int, input().split()) )
sum_arr = []

# 가장 큰 수의 위치와 그 값
max_idx_first = num_arr.index(max(num_arr))
max_value_first = num_arr.pop(max_idx_first)

# 다음 큰 수의 위치와 그 값
max_idx_second = num_arr.index(max(num_arr))
max_value_second = num_arr.pop(max_idx_second)

# 입력된 더해질 횟수 만큼 반복
for _ in range(M):
    # 제한된 횟수가 될시 다음 큰수 +
    if len(sum_arr) % K == 0 and len(sum_arr) != 0: 
        sum_arr.append(max_value_second)
    # 연속될 수 있는 횟수 만큼 가장큰수 +
    else: 
        sum_arr.append(max_value_first)
        
# 조건에 맞는 수를 담은 list의 합을 반환
print(sum(sum_arr))

# my code end


# 제공된 정리된 코드 start

# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력

# 제공된 정리된 코드 end