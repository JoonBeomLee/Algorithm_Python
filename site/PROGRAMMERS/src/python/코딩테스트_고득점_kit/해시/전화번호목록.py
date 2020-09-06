def solution(phone_book):
    answer = True
    #phone_book.sort(key=lambda x:len(x))
            
    for tgNum_idx in range(len(phone_book)):
        
        for search_idx in range(len(phone_book)):
            
            if tgNum_idx == search_idx: continue
            elif len(phone_book[tgNum_idx]) > len(phone_book[search_idx]): continue
            else:
                if phone_book[tgNum_idx] in phone_book[search_idx] and phone_book[tgNum_idx][0] == phone_book[search_idx][0]:
                    answer = False
                    return answer
    
    return answer