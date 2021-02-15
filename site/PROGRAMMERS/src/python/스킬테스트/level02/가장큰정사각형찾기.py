def solution(board):
    answer = 1234
    
    new_board = []
    
    for h_idx in range(len(board)):
        tmp_floor = []
        
        for w_idx in range(len(board[0])):
            
            # [i, j] = min([i-1, j-1], [i-1, j], [i,j-1]) + 1
            if board[h_idx][w_idx] != 0:
                board[h_idx][w_idx] = min(board[h_idx - 1][w_idx - 1], board[h_idx - 1][w_idx], board[h_idx][w_idx - 1]) + 1

    answer = max(max(board))   
        
    return answer * answer