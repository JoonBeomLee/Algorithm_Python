# input N, M
N, M = map(int, input().split())

# input 2D map
ice_bucket = []
for i in range(N):
    ice_bucket.append(list(map(int, input())))

# DFS로 특정한 노드를 방문
# 뒤에 연결된 모든 노드들도 방문
def DFS(x, y):
    # ice_bucke 밖인 경우 종료
    if x <= -1 or x >= N or y <= -1 or y >= M: return False

    # 현재 노드 아직 미방문인 경우
    if ice_bucket[x][y] == 0:
        # 해당 노드 방문 처리
        ice_bucket[x][y] = 1

        # 상, 하, 좌, 우의 재귀적 호출
        DFS(x - 1, y)
        DFS(x, y - 1)
        DFS(x + 1, y)
        DFS(x, y + 1)

        return True

    return False

# 모든 빈칸에 얼음 채우기
result = 0

for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        if DFS(i, j) == True: result += 1

# 경계로 구분된 값을 카운트
print(result)