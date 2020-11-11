def solution(dartResult):
    answer = []
    tmp_score = 0
    ten_num_check = False
    
    for dart_idx in range(len(dartResult)):
        dart = dartResult[dart_idx]
        
        ## dart = num
        if dart.isdecimal():
            if ten_num_check: ten_num_check = False; continue
            else:
                answer.append(tmp_score)  
    
            tmp_score = int(dart)
            
            #check 10 num
            if tmp_score == 1:
                if dartResult[dart_idx+1] == "0":
                    tmp_score = 10
                    ten_num_check = True
        
        # dart = bonus
        elif dart in ["S", "D", "T"]:
            if dart == "S": tmp_score = tmp_score ** 1
            elif dart == "D": tmp_score = tmp_score ** 2
            elif dart == "T": tmp_score = tmp_score ** 3
        
        # dart = option
        elif dart in ["*", "#"]:
            if dart == "*":
                answer[-1] = answer[-1] * 2
                tmp_score = tmp_score * 2
                
            elif dart == "#":
                tmp_score = tmp_score * -1
                
        print(dart, answer)
        
    # last dart score add
    answer.append(tmp_score)
        
    return sum(answer)