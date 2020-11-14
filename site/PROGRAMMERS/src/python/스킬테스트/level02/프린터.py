def priority_check(job_info, jobs_list):
    out_check = True
    
    for job in jobs_list:
        if job_info[1] < job[1]: 
            out_check = False; 
            break
            
    return out_check

def solution(jobs, location):
    answer = 1
    jobs_list = []          # [0] job 원래 위치 | [1] job 중요도 
    
    for job_idx in range(len(jobs)):
        jobs_list.append([job_idx, jobs[job_idx]])
    
    while True:            
        # list가 1개만 남아 있을경우
        if len(jobs_list) <= 1: break
            
        # 중요도 체크
        # 현재 처리할 일이 대상 작업이라면 stop
        tg_job = jobs_list.pop(0)
        out_check = priority_check(tg_job, jobs_list)
        
        if tg_job[0] == location and out_check: break
        
        # 중요도 체크 - 대상 작업의 우선순위가 낮아 반환될 경우
        if out_check == False: jobs_list.append(tg_job)
        # 중요도 체크 - 대상 작업의 우선순위가 높아 작업 진행할 경우
        else: answer += 1
            
    return answer