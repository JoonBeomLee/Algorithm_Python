def solution(lottos, win_nums):
    answer = []
    match = 0
    zero = 0
    
    for lotto in lottos:
        if lotto == 0: 
            zero += 1
            continue
            
        if lotto in win_nums:
            match += 1
            
    print(match, zero)
    
    # 가장 높은 등수
    if match + zero == 6:
        answer.append(1)
    elif match + zero == 5:
        answer.append(2)
    elif match + zero == 4:
        answer.append(3)
    elif match + zero == 3:
        answer.append(4)
    elif match + zero == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    # 가장 낮은 등수
    if match == 6:
        answer.append(1)
    elif match == 5:
        answer.append(2)
    elif match == 4:
        answer.append(3)
    elif match == 3:
        answer.append(4)
    elif match == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    print(answer)
    
    return answer