def remove_judge(string):
    st_ch = string[0]
    st_pos = 0
    ed_pos = 0
    switch = 0
    
    for st_idx, strs in enumerate(string):            
        if st_ch == strs and switch != 2:
            ed_pos = st_idx
        
        elif switch == 1:
            break
        else:            
            switch += 1
            st_ch = strs
            st_pos = st_idx

    return st_pos, ed_pos
            
        
def solution(s):
    answer = 0

    while True:
        if len(s) == 0: 
            answer = 1
            break
        
        st_pos, ed_pos = remove_judge(s)
        
        if ed_pos == 0: break
        
        if st_pos != ed_pos:
            #print("check", end="\t")
            #print(st_pos, ed_pos)
            #print("pre :: ", s, s[st_pos:ed_pos+1])
            
            s = s[:st_pos] + s[ed_pos+1:]
        else: break
        
        #print("post", s)
        

    return answer