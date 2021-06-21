# 정수 N, M 입력
N, M = map(int, input().split())

# N개의 화폐단위 정보를 입력받기
COINS = []
for i in range(N):
    COINS.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블
DP = [10001] * (M + 1)

# 다이나믹 프로그래밍 진행(보텀업)
DP[0] = 0
for i in range(N):
    for j in range(COINS[i], M + 1):
        # (i - k) 원을 만드는 방법 존재 할 경우
        if DP[j - COINS[i]] != 10001:
            DP[j] = min(DP[j], DP[j - COINS[i]] + 1)

# 계산된 결과 출력
# 최종적으로 M원을 만드는 방법이 없는 경우
if DP[M] == 10001:
    print(-1)
else:
    print(DP[M])