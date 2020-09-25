def solution(numbers):
    answer = []
    
    for idx_a in range(len(numbers)):
        for idx_b in range(len(numbers)):
            if idx_a == idx_b: continue
            
            answer.append(numbers[idx_a] + numbers[idx_b])
            
    answer = list(set(answer))
    answer = sorted(answer)
    return answer