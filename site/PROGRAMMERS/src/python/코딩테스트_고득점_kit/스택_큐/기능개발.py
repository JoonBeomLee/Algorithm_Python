def solution(progresses, speeds):
    answer = []
    
    while True:
        # 처리할 작업이 없을경우 종료
        if not progresses: break
            
        print(progresses)
            
        done_count = 0
        for p_idx in range(len(progresses)):
            progresses[p_idx] += speeds[p_idx]
            
            if progresses[p_idx] >= 100: 
                del(progresses[p_idx])
                del(speeds[p_idx])
                done_count += 1
                
        if done_count:
            answer.append(done_count)
            
    return answer