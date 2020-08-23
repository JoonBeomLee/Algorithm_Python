from itertools import permutations

N, M = list(map(int, input().split()))
num_list = [_ for _ in range(1, N+1)]
permu_list = permutations(num_list, M)

for permu in permu_list:
    for num in permu:
        print(num, end=" ")
    print()    