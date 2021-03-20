import copy

def remove_box(M, N, board):
    remove = []
    
    for m in range(M):
        for n in range(N):
            # 경계선 pass
            if m == M - 1 or n == N - 1: continue
            
            target = board[m][n]
            right = board[m][n+1]
            down = board[m+1][n]
            dash = board[m+1][n+1]
            
            if target == "0": continue
            
            # 같은 block 판단
            if target == right and target == down and target == dash:
                
                if [m, n] not in remove: remove.append([m, n])
                if [m, n+1] not in remove: remove.append([m, n+1])
                if [m+1, n] not in remove: remove.append([m+1, n])
                if [m+1, n+1] not in remove: remove.append([m+1, n+1])
                
            #print(f"{board[m][n]}  ", end="")
    
    return remove

def fit_board(M, N, board, remove):
    r_count = 0
    
    # 삭제 반영
    for rm in remove:       
        board[rm[0]][rm[1]] = "0"
        # 제거 개수 카운트
        r_count += 1
            
    # new down logic
    # 가로 개수
    for n in range(N):
        # 세로 반환
        tmp = []
        for m in range(M):
            tmp.append(board[m][n])
            
        # 당기기
        tmp_idx = 0
        zero_list = []
        rst_list = []
        while True:
            # 전체 search 완료시 stop
            if tmp_idx > len(tmp) - 1: break
            
            # zero 추가
            if tmp[tmp_idx] == "0":
                # 삭제
                zero_list.append(tmp_idx)
            # 나머지값 추가    
            else:
                rst_list.append(tmp[tmp_idx])
            # 다음 대상 search    
            tmp_idx += 1
        
        tmp = zero_list + rst_list
        for m in range(M):
            board[m][n] = tmp[m]
        
    return r_count
    
    
def board_print(M, N, board):
    for m in range(M):
        for n in range(N):
            print(f"{board[m][n]}  ", end="")
        print()
        
def solution(m, n, board):
    answer = 0
    
    re_board = []
    
    # 문자열 배열화
    for b in board:
        re_board.append(list(b))
    board = re_board
    
    # 블럭 제거 시작
    while True:
        #print("======== pre board ========= \n")
        #board_print(m, n, board)
        remove = remove_box(m, n, board)
        
        # 삭제할 블럭 없을때 stop
        if len(remove) == 0: break
            
        r_blocks = fit_board(m, n, board, remove)
        #print("======== remove board ========= \n")
        #board_print(m, n, board)
        
        # 삭제 블럭 개수 반영
        answer += r_blocks
        
    return answer