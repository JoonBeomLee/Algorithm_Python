# 문제 점화식
# N_i = N_i-1 + N_i-2 x 2

# 정수 N을 입력받기
N = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
DP = [0] * 1001

# 다이나믹 프로그래밍 진행(보텀업)
DP[1] = 1
DP[2] = 3

for i in range(3, N + 1):
    DP[i] = (DP[i - 1] + DP[i - 2] * 2) % 796796

print(DP[N])