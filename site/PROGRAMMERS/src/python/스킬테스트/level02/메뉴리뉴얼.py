from itertools import combinations

def solution(orders, course):
    answer = 0
    
    # menu 조합
    combi = []
    for order in orders:
        for menu_len in range(2, len(order)+1):
                combi.extend(list(map(list, combinations(order, menu_len))))
    
    # course 개수별로 분류
    total_menu = []
    for cs in course:
        menu_list = {}
        
        for comb in combi: 
            if cs == len(comb):
                comb.sort()
                tmp_comb = ''.join(comb)
                
                if tmp_comb in menu_list:
                    menu_list[tmp_comb] += 1
                else:
                    menu_list[tmp_comb] = 1
                    
        items = list(map(list, sorted(((v, k) for k, v in menu_list.items()), reverse=True)))
        print(items)
    
    return answer