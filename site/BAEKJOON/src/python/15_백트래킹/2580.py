# sdk = [[0, 3, 5, 4, 6, 9, 2, 7, 8],
#             [7, 8, 2, 1, 0, 5, 6, 0, 9],
#             [0, 6, 0, 2, 7, 8, 1, 3, 5],
#             [3, 2, 1, 0, 4, 6, 8, 9, 7],
#             [8, 0, 4, 9, 1, 3, 5, 0, 6],
#             [5, 9, 6, 8, 2, 0, 4, 1, 3],
#             [9, 1, 7, 6, 5, 2, 0, 8, 0],
#             [6, 0, 3, 7, 0, 1, 9, 5, 2],
#             [2, 5, 8, 3, 9, 4, 7, 6, 0]]

import sys

sdk = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sdk[i][j] == 0]

def sdoku(index):
    
    # 한 바퀴에서 모든 경우를 다 보았으면 출력
    if index == len(zeros):
        for row in sdk:
            print(*row)
        sys.exit(0)
    else:
        x = zeros[index][0]
        y = zeros[index][1]
        dx = (x//3) * 3
        dy = (y//3) * 3

        # 사용할 수 있는 숫자 9개
        num_list = [False] + [True for _ in range(9)]

        for j in range(9):
            # 가로 검사
            # 세로 검사
            if(sdk[x][j]):
                num_list[sdk[x][j]] = False       
            if(sdk[j][y]):
                num_list[sdk[j][y]] = False

        # 3*3 box 검사
        for i in range(dx, dx + 3):
            for j in range(dy, dy + 3):
                check_num = sdk[i][j]
                if(check_num):
                    num_list[check_num] = False

        # 현재 가능한 수만 가져옴
        # 가능한 수를 가져왔으면, 이전에 다뤄왔던 백트래킹을 사용하면 됨
        candidate_list = [i for i, k in enumerate(num_list) if k]
        
        # 경우의 수 고려
        for num in candidate_list:
            sdk[x][y] = num
            sdoku(index + 1)
            sdk[x][y] = 0
sdoku(0)