num_str = list(map(int, input()))
num_str.sort(reverse=True)

for _ in num_str:
    print(f'{_}', end="")