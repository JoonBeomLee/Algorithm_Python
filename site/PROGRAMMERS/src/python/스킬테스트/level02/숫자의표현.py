def solution(n):
    answer = 0
    answer_list = [0 for _ in range(n)]
    
    for st_num in range(1, n+1):
        tmp_result = 0
        tmp_list = []
        tmp_num = st_num
        
        #print("\n\n============================")
        #print("st_num :: ", st_num)
        
        while True:
            # condition[sum = n] success
            # condition[sum > n] fail
            if tmp_result >= n: break
                
            tmp_result += tmp_num
            tmp_list.append(tmp_num)
            tmp_num += 1
        
        if tmp_result == n: 
            #print(tmp_list)
            answer += 1
            
    
    return answer