def solution(gems):
    answer = []
    gems_packs = {}
    
    st_idx, ed_idx = 0, 0
    gems_len = len(gems) + 1
    gems_sort_count = len(set(gems))
    
    # 마지막 보석까지
    while ed_idx < len(gems):
        
        # 뒷 부분 index 증가
        if gems[ed_idx] not in gems_packs:
            gems_packs[gems[ed_idx]] = 1
        else:
            gems_packs[gems[ed_idx]] += 1
            
        ed_idx += 1    
        
        # 모든 보석이 채워졌을 경우
        # 최소 범위를 찾기위해
        # 앞부분 증가하며 나감
        if len(gems_packs) == gems_sort_count:
            while st_idx < ed_idx:
                if gems_packs[gems[st_idx]] > 1:
                    gems_packs[gems[st_idx]] -= 1
                    st_idx += 1
                    
                elif gems_len > ed_idx - st_idx:
                    gems_len = ed_idx - st_idx
                    answer = [st_idx + 1, ed_idx]

                    break
                
                else: break
                    
                        
    return answer