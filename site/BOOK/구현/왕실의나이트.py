# 처음 나이트의 위치
input_pos = input()
row = int(input_pos[1])
# col = a ~ h 변환위함
# 체스판 8 x 8
col = int(ord(input_pos[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향
move_dir = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 결과값
count = 0

# 8가지 방향이 이동 가능한지 확인
# 맵을 넘어서면 안된다.
for move in move_dir:
    # 이동할 위치
    next_row = row + move[0]
    next_col = col + move[1]

    # 유효한 위치인경우 count ++
    if next_row >= 1 and next_rnow <= 8 and next_col >= 1 and next_col <= 8:
        count += 1

# 결과값 출력
print(count)