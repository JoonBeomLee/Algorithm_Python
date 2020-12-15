def solution(name):
    answer = 0
    init_name = ["A" for _ in range(len(name))]
    print(init_name)
    
    # A -> ord('A') = 65
    # Z -> ord('Z') = 90
    for i_n, n in zip(init_name, name):
        print(i_n, n)
        
        if i_n != n :
            answer += abs(ord(i_n) - ord(n))
            
        answer += 1
        
    print(answer)
    
    return answer - 1