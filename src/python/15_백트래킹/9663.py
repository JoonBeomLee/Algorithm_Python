N = int(input())
grid = [[True for _ in range(N)] for _ in range(N)]

def dfs_queen():
    queen_count = 0
    
    def put_queen(i, j, board):
        right_up_dash = i + j
        right_down_dash = abs(i - j)
        
        for row in range(N):
            for col in range(N):
                if row == i: 
                    board[row][col] = False
                elif col == j: 
                    board[row][col] = False
                elif row + col == right_up_dash:
                    board[row][col] = False
                elif abs(row-col) == right_down_dash:
                    board[row][col] = False

        
    def check_board(x, y):
        board = [[True for _ in range(N)] for _ in range(N)]
        count = 1
        print(f'======== check_board start ========')
        print(f'queen pos : board[{x}][{y}]')
        put_queen(x, y, board)
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    print(f'queen pos : board[{i}][{j}]')
                    put_queen(i, j, board)
                    count += 1
        print(f'======== check_board end count :: {count} ========\n\n')
        return count
    
    def check_grid():
        total_count = 0
        
        for grid_x in range(N):
            for grid_y in range(N):
                grid[grid_x][grid_y] = False
                total_count += check_board(grid_x, grid_y)
        
        return total_count
    
    queen_count = check_grid()
    print(queen_count)
    
print("search start")
dfs_queen()