A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
C = list(map(int, input().split(" ")))

X_list = {}
Y_list = {}
for X in (A[0], B[0], C[0]):
    try:
        X_list[X] += 1
    except:
        X_list[X] = 0
    
for Y in (A[1], B[1], C[1]):
    try:
        Y_list[Y] += 1
    except:
        Y_list[Y] = 0
    
print([X for X, values in X_list.items() if values == 0][0], end=" ")
print([Y for Y, values in Y_list.items() if values == 0][0], end=" ")