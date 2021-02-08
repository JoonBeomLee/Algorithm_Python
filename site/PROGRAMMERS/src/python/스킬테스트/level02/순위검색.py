from itertools import combinations

def solution(info, query_list):
    answer = []
    info_db = filter_info(info)
    
    for query in query_list:
        reAssign_query = query.replace("and", " ").split()
        # score 제외한 query 재정렬 = info와 같은 규칙 [condition/condition....]
        q_score = int(reAssign_query[-1])
        reAssign_query = '/'.join(reAssign_query[:-1])
        
        # 검색할 query가 대상에 있다면
        if reAssign_query in info_db:
            # 조건에 맞는 score list 반환
            search_score_list = info_db[reAssign_query]
            
            if len(search_score_list) > 0:
                st, ed = 0, len(search_score_list)
                
                while st != ed and st != len(search_score_list):
                    if search_score_list[(st + ed) // 2] >= q_score:
                        ed = (st + ed) // 2
                    else: 
                        st = (st + ed) // 2 + 1
                        
                # 조건에 맞는(query의 score 보다 큰) socre index 부터 끝까지 
                # score_list는 오름차순 정렬 되어잇음
                answer.append(len(search_score_list) - st)
        # 검색 query가 대상에 없다면       
        else:
            answer.append(0)
            
    return answer


# 입력된 info 
# 조건에 맞게 재정렬
# 중복되는 info 처리 위함
# 효율성 문제 해결가능
def filter_info(info_list):
    filter_info = {}
    
    for info in info_list:
        tmp = info.split()
        
        conditions = tmp[:-1]      
        score = int(tmp[-1])
        
        for n in range(5):
            # 4개의 경우에서  ~ 4 까지의 조합
            combi = list(combinations(range(4), n))
            
            # '-'의 조합만큼 loop
            for comb in combi:
                tmp_combi = conditions.copy()
                
                # '-' 인덱스 위치 반환
                for c_idx in comb:
                    tmp_combi[c_idx] = '-'
                
                # '-' 가 배치된 info 를 '/' 를 구분으로 한줄로 재정렬
                reAssign_info = '/'.join(tmp_combi)
                
                # 기존에 있는 info일 경우 score 추가등록
                if reAssign_info in filter_info:
                    filter_info[reAssign_info].append(score)
                # 새로운 info 일 경우 dictionary 에 info, score 등록
                else:
                    filter_info[reAssign_info] = [score]
                    
    # 재정렬된 info 
    # score로 다시한번 정렬
    for score in filter_info.values():
        score.sort()
        
    return filter_info