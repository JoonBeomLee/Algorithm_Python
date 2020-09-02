star_cnt = int(input())

for height in range(star_cnt*2):
    # input 1 
    if star_cnt == 1: print('*'); break
    
    # input other
    for width in range(star_cnt):
        # 홀수
        if height % 2 == 1:
            print( '*'  if width%2 == 1 else ' ', end='')
        # 짝수
        else:
            print( ' '  if width%2 == 1 else '*', end='')
    print()