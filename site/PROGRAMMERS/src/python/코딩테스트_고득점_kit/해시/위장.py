import collections

def filter_clothes(data):
    return data[1]

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
    
    print(tmp_list)
    
    return answer