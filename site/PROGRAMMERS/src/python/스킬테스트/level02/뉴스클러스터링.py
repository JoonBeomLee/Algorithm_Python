import copy

def seted_str(string):
    string = string.lower()
    st_list = []
    
    for st_idx, st in enumerate(string):
        # 마지막 문자 pass
        if st_idx == len(string) - 1: break
            
        if st.isalpha() and string[st_idx+1].isalpha():
            st_list.append(f"{st}{string[st_idx+1]}")
            
    return st_list

def solution(str1, str2):
    answer = 0
    
    seted_str1 = seted_str(str1)
    seted_str2 = seted_str(str2)
    
    if len(seted_str1) > len(seted_str2):
        intersection = len([seted_str1.remove(st) for st in seted_str2 if st in seted_str1])
    else:
        intersection = len([seted_str2.remove(st) for st in seted_str1 if st in seted_str2])
        
    union = len(seted_str1) + len(seted_str2)    

    if intersection == 0 and union == 0:
        answer = 65536
    else: 
        answer = int((intersection / union) * 65536)
    
    return answer