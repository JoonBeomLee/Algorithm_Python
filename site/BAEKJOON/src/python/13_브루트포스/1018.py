N, M = map(int, input().split())
chess = []

# init chess
for _ in range(int(N)):
    tmp = str(input()) 
    chess.append(tmp)

min_num = None

for i in range(N - 7):
    for j in range(M - 7):
        count_W, count_B = 0, 0
        
        # W 로 시작할 경우
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if((k + l - i - j) % 2 == 0):
                    if(chess[k][l] == 'B'):
                        count_W += 1
                else:
                    if(chess[k][l] == 'W'):
                        count_W += 1
                        
        # B  경우      
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if((k + l - i - j) % 2 == 0):
                    if(chess[k][l] == 'W'):
                        count_B += 1
                else:
                    if(chess[k][l] == 'B'):
                        count_B += 1
                        
        change_box = min(count_W, count_B)
        if(min_num is None):
            min_num = change_box
        else:
            min_num = min(change_box, min_num)
            
print(min_num)