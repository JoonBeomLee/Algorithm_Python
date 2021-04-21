def strToMs(time):
    hhmmss = time.split(".")[0]
    ms = int(time.split(".")[1])
    
    h = int(hhmmss.split(":")[0])
    m = int(hhmmss.split(":")[1])
    s = int(hhmmss.split(":")[2])
    
    total_ms = (h * 3600 + m * 60 + s) * 1000 + ms
    
    return total_ms
    
def solution(lines):
    answer = 1
    boundary = []
    
    # data preprocess
    for line in lines:
        data = line.split()
        
        date = data[0]
        time = data[1]
        thresh = float(data[2].split("s")[0]) * 1000
        
        ed_ms = strToMs(time)
        st_ms = int(ed_ms - thresh + 1)
        
        boundary.append([st_ms, ed_ms])
    
    # 판단
    for b1_idx, b1 in enumerate(boundary):
        tmp_ans = 1
        
        for b2_idx, b2 in enumerate(boundary):
            if b2_idx < b1_idx + 1: continue
                     
            if b1[1] + 1000 > b2[0]: tmp_ans += 1
                
        answer = tmp_ans if tmp_ans > answer else answer
        
    
    return answer