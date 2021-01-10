# input N, M
N, M = map(int, input().split())

# 결과값
result = 0

# N x M 카드 입력
for i in range(N):
    # 한 행 입력
    card_list = list(map(int, input().split()))

    # 현재 행에서 최소값 찾기
    min_card = min(card_list)

    # 최소값 중에서 가장 큰 카드 찾기
    result = max(result, min_card)

print(result)