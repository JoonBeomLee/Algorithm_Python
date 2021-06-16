# 정수 N입력
N = int(input())

# 모든 식량 정보 입력받기
food_list = list(map(int, input().split()))

# 앞서 계산된 결과 저장 위한 DP
DP = [0] * 100

# 다이나믹 프로그래밍 진행 (보텀업)
DP[0] = food_list[0]
DP[1] = food_list[1]

for i in range(2, N):
    DP[i] = max(DP[i - 1], DP[i - 2] + food_list[i])

# 계산 결과
print(DP[N - 1])