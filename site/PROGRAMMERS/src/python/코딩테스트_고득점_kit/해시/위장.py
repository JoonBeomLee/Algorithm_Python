import collections

def solution(clothes):
    answer = 0
    catg_list = []
    
    clothes.sort(key=lambda x:(len(x), x[0]))
    for clothe in clothes:
        catg_list.append(clothe[1])
        
    catg_dict = collections.Counter(catg_list)
    tmp_list = []
    for ctg in collections.Counter(catg_list):
        tmp_list.append([ x for x in range(int(catg_dict[ctg])) ])
    
    if len(tmp_list) == 1: 
        answer = len(tmp_list[0])
    elif len(tmp_list) == 2:
        answer_tmp = 1
        for tmp in tmp_list:
            answer += len(tmp)    
            answer_tmp *= (len(tmp))
            
        answer = answer + answer_tmp
    else:
        answer_tmp = 1
        for tmp in tmp_list:
            answer += len(tmp)    
            answer_tmp *= (len(tmp) + 1)
        
    return answer