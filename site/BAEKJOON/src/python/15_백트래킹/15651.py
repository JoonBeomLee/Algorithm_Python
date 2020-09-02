# 중복 순열
from itertools import product

N, M = list(map(int, input().split()))
num_list = [_ for _ in range(1, N+1)]
product_list = product(num_list, repeat=M)

for prod in product_list:
    for num in prod:
        print(num, end=" ")
    print()    