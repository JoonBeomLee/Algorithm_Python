# N, K 입력
N, K = map(int, input().split())

# 반복횟수
count = 0

# N이 1이 될때 까지
while True:
    # 1이 되면 탈출
    if N == 1: 
        break

    # 2. N을 K로 나눈다
    if N % K == 0:
        N = N / K
    # 2가 불가능 할 경우
    # 1. N 에서 1을 뺀다
    else:
        N = N - 1

    # 1 or 2 작업횟수 카운트
    count += 1

# 결과 출력
print(count)


# ------------------------- 책 답안
# N, K 입력
N, K = map(int, input().split())

# 반복횟수
count = 0

# N이 1이 될때 까지
while True:
    # N == K로 나누어 떨어지는 수 가 될떄 까지 1씩 빼기
    target = (N // K) * K
    
    count += N - target
    N = target
    # N이 K보다 작을때(더이상 나눌 수 없을 때) 반복문 탈출
    if N < K: break

    # K로 나누기
    count += 1
    N //= K

# 마지막으로 남은 수에 대하여 1씩 빼기
count += N - 1
# 결과 출력
print(count)