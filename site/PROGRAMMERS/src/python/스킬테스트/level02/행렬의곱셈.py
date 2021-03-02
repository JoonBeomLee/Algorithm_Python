def solution(arr1, arr2):
    answer = [[]]
    
    arr1_w, arr1_h = len(arr1[0]), len(arr1)
    arr2_w, arr2_h = len(arr2[0]), len(arr2)
    
    answer = [[0 for _ in range(arr2_w)] for _ in range(arr1_h)]
    
    for r_idx in range(len(arr1)):
        
        for c_idx in range(len(arr2[0])):
            
            for k in range(len(arr1[0])):
                answer[r_idx][c_idx] += (arr1[r_idx][k] * arr2[k][c_idx])

    
    return answer