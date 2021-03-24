from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    # 열의 조합 - 전체 조합
    candi_list = []
    for idx in range(1, col + 1):
        candi_list.extend(combinations(range(col), idx))
        
    # 유일성 체크 
    # 열의 조합으로 각각의 행을 표현할수 있을 경우
    uniq_list = []
    for candi in candi_list:
        tmp_list = [tuple([row[idx] for idx in candi]) for row in relation]
        
        # 해당 조합의 열로 각각의 행 표현 가능할경우 추가
        if len(set(tmp_list)) == row:
            uniq_list.append(candi)
            
    # 최소성 체크
    answer = set(uniq_list)
    
    for A in range(len(uniq_list)):
        for B in range(A + 1, len(uniq_list)):            
            if len(uniq_list[A]) == len(set(uniq_list[A]) & set(uniq_list[B])):
                answer.discard(uniq_list[B])

    return len(answer)