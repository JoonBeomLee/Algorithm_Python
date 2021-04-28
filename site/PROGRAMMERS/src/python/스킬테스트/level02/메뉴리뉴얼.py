from itertools import combinations

def solution(orders, course):    
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
        
        # skip empty list
        if len(items) == 0: continue
            
        max_menu = items.pop(0)
        
        # skip 1 count menu
        if max_menu[0] == 1: continue
            
        total_menu.append(max_menu[1])
        
        for item in items:
            if max_menu[0] == item[0]:
                total_menu.append(item[1])
                
    total_menu.sort()
    print(total_menu)
    
    return total_menu