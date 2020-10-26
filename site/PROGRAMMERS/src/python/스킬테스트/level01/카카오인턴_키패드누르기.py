def find_idx(element, matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                result = [i, j]
                
    return result

def solution(numbers, hand):
    answer = ""
    pad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]
    # cur_pos[0] 왼손 | cur_pos[1] 오른손 위치
    cur_pos = [find_idx("*", pad), find_idx("#", pad)]
    
    for num in numbers:        
        # 1 4 7 일 경우 L
        if num in [1, 4, 7]:
            answer += "L"
            cur_pos[0] = find_idx(str(num), pad)
        
        # 3 6 9 일 경우 R 
        elif num in [3, 6, 9]:
            answer += "R"
            cur_pos[1] = find_idx(str(num), pad)
        
        # 2 5 8 0 일 경우 위치 확인
        else:
            tg_pos = find_idx(str(num), pad)
            
            left_dist = abs(cur_pos[0][0] - tg_pos[0]) + abs(cur_pos[0][1] - tg_pos[1])
            right_dist = abs(cur_pos[1][0] - tg_pos[0]) + abs(cur_pos[1][1] - tg_pos[1])
            
            if left_dist > right_dist: 
                answer += "R"
                cur_pos[1] = tg_pos
                
            elif left_dist == right_dist: 
                answer += hand[0].upper()
                if(hand[0] == "r"): cur_pos[1] = tg_pos
                elif(hand[0] == "l"): cur_pos[0] = tg_pos
                    
            elif left_dist < right_dist: 
                answer += "L"
                cur_pos[0] = tg_pos
            
    return answer