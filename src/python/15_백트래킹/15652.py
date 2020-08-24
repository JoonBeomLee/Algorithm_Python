from itertools import combinations_with_replacement

N, M = list(map(int, input().split()))
num_list = [_ for _ in range(1, N+1)]
combi_list = list(combinations_with_replacement(num_list, M))

for combi in combi_list:
    for num in combi:
        print(num, end=" ")
    print()