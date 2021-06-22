import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# 노드의 개수, 간선의 개수 입력
N, M = map(int, input().split())
# 시작 노드 번호 입력
st_node = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(N + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 생성
visited = [False] * (N + 1)
# 최단 거리 테이블을 모두 무한으로 생성
distance = [INF] * (N + 1)

# graph 생성
for _ in range(M):
    # st 에서 ed 까지 dist 만큼 거리
    st, ed, dist = map(int, input().split())
    graph[st].append((ed, dist))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_val = INF
    idx = 0 # 가장 최단 거리가 짧은 노드(인덱스)

    for i in range(1, N + 1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i 