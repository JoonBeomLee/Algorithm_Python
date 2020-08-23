from itertools import combinations

N, M = list(map(int, input().split()))
num_list = [_ for _ in range(1, N+1)]
combi_list = combinations(num_list, M)

for combi in combi_list:
    for num in combi:
        print(num, end=" ")
    print()    