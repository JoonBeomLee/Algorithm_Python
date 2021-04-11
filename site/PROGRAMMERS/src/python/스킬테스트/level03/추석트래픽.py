from datetime import datetime, timedelta

def solution(lines):
    answer = 0
    traffic = {}
    date_day = "2016-09-15"
    
    for job_idx, line in enumerate(lines):
        sp_line = line.split()
        
        T = float(sp_line[2].split("s")[0])
        ST_time = sp_line[1].split(".")[0]
        ST_s_datetime = "0." + sp_line[1].split(".")[1] + "000"
        ST_s = float("0." + sp_line[1].split(".")[1])
        ED_s = int(ST_s + T)
        
        traffic_time = ""
        
        tmp_date_s = f"{date_day} {ST_time}"
        tmp_dt = datetime.strptime(f"{ST_time}{ST_s_datetime}", '%Y-%m-%d %H:%M:%S.%f')
        
        print(tmp_dt)
        

    
    return answer