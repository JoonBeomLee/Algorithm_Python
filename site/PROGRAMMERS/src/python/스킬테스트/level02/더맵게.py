def check_scoville(scov_arr, k):
    for scov in scov_arr:
        if scov <= k: 
            return False
    
    return True

def solution(scoville, K):
    mix_count = 0
    
    while True:
        # 예외처리
        # 개수는 적은데
        # k조건은 만족시키지 못할 떄 -1
        if len(scoville) <= 1 and not check_scoville(scoville, K): 
            mix_count = -1
            break
            
        # loop 제한
        if check_scoville(scoville, K): break
        
        # 최소 스코빌 지수
        min_scoville = min(scoville)
        
        # 최소 스코빌 지수 pop
        min_idx_scoville = scoville.index(min_scoville)
        del scoville[min_idx_scoville]
        
        # 2번째 적은 스코빌 지수
        next_min_scoville = min(scoville)
        next_min_idx_scoville = scoville.index(next_min_scoville)
        
        # 1_scov + (2_scov * 2)
        scoville[next_min_idx_scoville] = min_scoville + (next_min_scoville * 2)
        
        # mix_count ++ 
        mix_count += 1
        
    return mix_count