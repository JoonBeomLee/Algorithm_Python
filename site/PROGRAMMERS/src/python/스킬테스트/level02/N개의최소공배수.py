def solution(arr):
    answer = 0
    
    arr.sort()    
    answer = arr[-1] * arr[1]
    
    while True:        
        
        check_idx = 0
        for check in arr:
            if answer % check == 0:   
                check_idx += 1
            
        if check_idx == len(arr):
            break
            
        answer += 1
    
    return answer