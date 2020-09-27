def solution(answers):
    result = {}
    f_answer = []
    
    p_idx = 1
    p_1 = [1,2,3,4,5]
    p_2 = [2,1,2,3,2,4,2,5]
    p_3 = [3,3,1,1,2,2,4,4,5,5]
    p_total = [p_1, p_2, p_3]
    
    for p_arr in p_total:
        count = 0
        p_arr_idx = 0
        p_arr_idx_ed = len(p_arr)
        
        for answer in answers:
            if p_arr[p_arr_idx] == answer: count += 1
            
            p_arr_idx += 1
            if p_arr_idx == p_arr_idx_ed: p_arr_idx = 0
                
        result[p_idx] = count
        p_idx += 1
    
    for p_idx, p_score in result.items():       
        if p_score == max(result.values()):
            f_answer.append(p_idx)
    
    return f_answer