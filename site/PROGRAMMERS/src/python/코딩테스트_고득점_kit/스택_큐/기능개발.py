def solution(progresses, speeds):
    answer = []
    job_scheduler = [x for x in progresses]
        
    print(job_scheduler)
    
    """"""
    while True:
        # 처리할 작업이 없을경우 종료
        if not job_scheduler: break
            
        print(progresses)
            
        done_count = 0
        for p_idx in range(len(progresses)):
            job_scheduler[p_idx] += speeds[p_idx]
            
            if job_scheduler[p_idx] >= 100: 
                del(job_scheduler[p_idx])
                done_count += 1
                
        if done_count:
            answer.append(done_count)
    
    return answer