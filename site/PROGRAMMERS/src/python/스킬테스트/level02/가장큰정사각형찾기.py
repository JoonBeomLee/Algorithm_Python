global board

def solution(in_board):
    global board
    
    answer = []
    board = in_board
    
    for h in range(len(board)):
        
        for w in range(len(board[0])):
            
            # board[h][w] not empty -> check square
            if board[h][w] != 0:
                answer.append(check_square(h, w))
                
    return max(answer)
            
def check_square(st_h, st_w):
    global board
    
    tmp_sqaure = []
    tmp_width = []
    
    for h in range(st_h, len(board)):
        tmp_width = 0
        
        if board[h][st_w] == 0: break
        
        for w in range(st_w, len(board[0])):
                
            if board[h][w] == 0: break
            else:
                tmp_width += 1
                
        tmp_sqaure.append(tmp_width)
    
    if len(tmp_sqaure) == sum(tmp_sqaure) // len(tmp_sqaure):
        return sum(tmp_sqaure)
    else:
        return 0
