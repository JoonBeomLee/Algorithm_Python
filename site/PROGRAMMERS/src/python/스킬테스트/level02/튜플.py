def solution(string):
    answer = []
    tmp_list = []
    tmp_num = ''
    result = []
    
    for strs in string:          
        if strs == '{': continue
            
        if strs != ',':  
            if strs != '}':
                tmp_num += strs
            
        if strs == ',' or strs == '}':
            if tmp_num == '': continue
            
            tmp_list.append(int(tmp_num))
            tmp_num = ''
            
        if strs == '}':
            answer.append(tmp_list)
            tmp_list = []
    
    answer.sort(key=lambda x: len(x))
    
    for ans in answer:
        
        for an in ans:
            
            if int(an) not in result: result.append(int(an))
    
    return result