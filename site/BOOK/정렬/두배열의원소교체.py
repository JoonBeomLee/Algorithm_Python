N, K = map(int(input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

# 두 배열의 원소를 최대 K번 비교
for i in range(K):
    # A의 원소가 B의 원소보다 작은 경우
    if A[i] < B[i]:
        # 두 원소 교체
        A[i], B[i] = B[i], A[i]
    else:
        # A, B의 원소가 같거나 클때 반복문 탈출
        break

print(sum(A))