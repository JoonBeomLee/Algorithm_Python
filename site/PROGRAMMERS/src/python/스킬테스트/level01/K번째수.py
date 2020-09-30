def solution(array, commands):
    answer = []
    
    for cmd in commands:
        st = cmd[0] - 1
        ed = cmd[1]
        idx = cmd[2] - 1
        
        if st == ed: tmp = array[st]
        else:
            tmp_arr = sorted(array[st:ed])
            tmp = tmp_arr[idx]
            
        
        answer.append(tmp)
    return answer