def solution(progresses, speeds):
    answer = []
    jobs_day = []
    
    for prog, speed in zip(progresses, speeds):
        work_time = (100 - prog) // speed
        
        # 소수점으로 작업이 남을경우 + 1day
        if (100 - prog) % speed > 0: work_time += 1
        jobs_day.append(work_time)
    
    for d_idx, day in enumerate(jobs_day):
        if d_idx == 0: 
            max_time = day
            answer.append(1)
            continue
            
        # max보다 적을경우 이전값 +1
        if day <= max_time: answer[-1] += 1
        else:
            max_time = day
            answer.append(1)
            
    return answer