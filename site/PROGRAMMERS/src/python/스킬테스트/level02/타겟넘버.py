# DFS 함수 
# 결과 합산 위한 전역 변수 선언
answer = 0

def DFS(idx, numbers, target, value):
    # 전역 변수 사용 선언
    global answer
    
    N = len(numbers)
    # 마지막 노드
    # 정답인 경우
    if(idx == N and target == value):
        answer += 1
        
        return
    # 마지막 노드 
    # 정답 아닌경우
    if(idx == N): return
    
    # DFS탐색
    # + Node
    DFS(idx+1, numbers, target, value+numbers[idx])
    # - Node
    DFS(idx+1, numbers, target, value-numbers[idx])

def solution(numbers, target):
    # 전역 변수 사용 선언
    global answer
    
    # 시작 위치, num_list, target, sum_value
    DFS(0, numbers, target, 0)
    
    return answer