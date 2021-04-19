from datetime import datetime
from datetime import timedelta

def tsToDs(ts):
    #timestamp to datetime
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

def dsToTs(ds):
    #datetime to timestamp
    obj_datetime = datetime.strptime(ds, '%Y-%m-%d %H:%M:%S.%f')
    return obj_datetime

def addMSeconds(date, ms):
    return date + timedelta(milliseconds=ms)

def addSeconds(date, seconds):
    return date + timedelta(seconds=seconds)

def second2miliseconds(seconds):
    seconds = float(seconds.split("s")[0])
    
    return seconds * 1000

def solution(lines):
    answer = 0
    t_dict = {}
    
    # data reporcess
    for line in lines:
        line = line.split()
        
        DATE = line[0]
        ST = line[1]
        T = line[2]
        
        st_stamp = dsToTs(f"{DATE} {ST}")
        wk_stamp = addMSeconds(st_stamp, second2miliseconds(T))
        
        # 소요시간
        T_time = wk_stamp - st_stamp
        T_time_sp = str(T_time).split(":")
        T_time_sp = ":".join(T_time_sp[:2])
        # ms포함일 경우
        if "." in str(T_time): 
            T_time_ms = str(T_time).split(":")[2].split(".")[1][:-3]
        else:
            T_time_ms = 0
        T_time_s = str(T_time).split(":")[2].split(".")[0]
        
        #print(T_time, int(T_time_s), T_time_ms)
        
        total_time = 0

        while True:
            # total time이 주어진시간이 초과 될때
            if total_time == int(T_time_s):
                if float(T_time_ms) >= 0:
                    add_stamp = addSeconds(st_stamp, total_time + 1)
                    dict_stamp = str(add_stamp).split()[1]
                    
                    if "." in dict_stamp:
                        dict_stamp = dict_stamp.split(".")[0]
                        
                    if dict_stamp not in t_dict:
                        t_dict[dict_stamp] = 1
                    else:
                        t_dict[dict_stamp] += 1
                break
                
            #print(st_stamp)
            add_stamp = addSeconds(st_stamp, total_time)
            dict_stamp = str(add_stamp).split()[1]
            
            if "." in dict_stamp:
                dict_stamp = dict_stamp.split(".")[0]
            
            if dict_stamp not in t_dict:
                t_dict[dict_stamp] = 1
            else:
                t_dict[dict_stamp] += 1
    
            total_time += 1
    
    print(t_dict)
    
    return answer