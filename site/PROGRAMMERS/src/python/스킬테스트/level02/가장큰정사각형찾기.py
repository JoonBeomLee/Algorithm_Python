def solution(board):
    answer = 0
    
    for h_idx in range(len(board)):
        
        for w_idx in range(len(board[0])):
            
            # [i, j] = min([i-1, j-1], [i-1, j], [i,j-1]) + 1
            if board[h_idx][w_idx] != 0:
                
                left = board[h_idx][w_idx - 1] if w_idx - 1 >= 0 else 0  
                up = board[h_idx - 1][w_idx]  if h_idx - 1 >= 0 else 0
                dash = board[h_idx - 1][w_idx - 1] if h_idx - 1 >= 0 and w_idx - 1 >= 0 else 0
                
                board[h_idx][w_idx] = min(dash, left, up) + 1

    answer = max(map(max, board))
        
    return answer * answer