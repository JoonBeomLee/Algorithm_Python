def solution(N, stages):
    answer = []
    score_dict = {}
    rest_player = len(stages)
    
    for stage in range(N):
        tmp_count = stages.count(stage+1)
        percent = 0
        
        if not rest_player == 0: 
            percent = tmp_count / rest_player
            
        score_dict[stage+1] = percent
        rest_player -= tmp_count
    
    score_dict = sorted(score_dict.items(), key=lambda item: item[1], reverse=True)
    answer = [key[0] for key in score_dict]
    
    return answer