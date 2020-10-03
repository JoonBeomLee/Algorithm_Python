def solution(arr):
    answer = []
    
    for a_idx in range(len(arr)-1):
        if arr[a_idx] != arr[a_idx+1]:
            answer.append(arr[a_idx])
            
    answer.append(arr[len(arr)-1])
    
    return answer