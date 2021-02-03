def solution(info_list, query_list):
    answer = []
    
    for query in query_list:
        # query reprocessing
        query = query.replace("and", " ")
        query_split = query.split()
        
        query_result = 0
        
        for info in info_list:
            # info reprocessing
            info = info.replace("and", " ")
            info_split = info.split()
            
            print(query_split, "\t\t", info_split)
            
            # langauge check
            if query_split[0] != "-":
                if query_split[0] != info_split[0]: continue
                
            # position check
            if query_split[1] != "-":
                if query_split[1] != info_split[1]: continue
                
            # career check
            if query_split[2] != "-":
                if query_split[2] != info_split[2]: continue
                
            # food check
            if query_split[3] != "-":
                if query_split[3] != info_split[3]: continue
                
            # score check
            if query_split[4] != "-":
                if query_split[4] > info_split[4]: continue
                
            query_result += 1
            
        answer.append(query_result)
    
    return answer