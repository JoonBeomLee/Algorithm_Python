N = int(input())
board = [0 for _ in range(N)]
queen_count = 0

def validation_board(row):
    if row < 1: return True
    for i in range(row):
        if board[row] == board[i] or row - i == abs(board[row] - board[i]): return False
    
    return True

def NQueen_v2(row = 0):
    global queen_count
    
    for i in range(N):
        board[row] = i
        
        if validation_board(row):
            if row == N - 1:
                print(board)
                queen_count += 1
            else:
                NQueen_v2(row+1)

def NQueen_v1(row=-1):
    global queen_count
    
    if validation_board(row):
        if row == N - 1: 
            print(board)
            queen_count += 1
        else:
            for i in range(N):
                board[row + 1] = i
                NQueen_v1(row+1)
                
NQueen_v2()
print(queen_count)                