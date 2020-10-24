def solution(arr):
    answer = []
    
    if len(arr) == 1 : 
        answer = [-1]
        return answer
    
    arr_min = min(arr)
    
    for arr_idx in arr:
        if arr_idx != arr_min: answer.append(arr_idx)
        else: continue
    
    return answer