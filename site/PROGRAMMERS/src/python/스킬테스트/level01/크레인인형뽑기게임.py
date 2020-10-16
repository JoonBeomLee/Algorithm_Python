def check_cago(arr, count):
    # 하나 이하일 경우 종료
    if len(arr) < 2: return arr
    
    # 두 개가 연속할 경우
    while True:
        dupl_idx = -1
        
        for idx in range(len(arr)-1):
            if arr[idx] == arr[idx+1]:           
                dupl_idx = idx 
                break
                
        if dupl_idx != -1:
            del arr[dupl_idx]
            del arr[dupl_idx]
            
            count += 2
        
        else: break
                 
    return arr, count

def solution(board, moves):
    answer = 0
    cago = []
    
    for move in moves:
        move -= 1   # 1 부터 시작
        
        for depth in range(len(board)):
            # 인형 체크 => 인형 있을 경우 추출
            if(board[depth][move] != 0):
                cago.append(board[depth][move])
                board[depth][move] = 0
                
                break
    cago, answer = check_cago(cago, answer)        
            
    return answer