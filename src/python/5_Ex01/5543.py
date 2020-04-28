ham_list = []
bev_list = []

for i in range(5):
    cnt = int(input())
    
    if i < 3:
        ham_list.append(cnt)
    else:
        bev_list.append(cnt)

min_set = min(ham_list) + min(bev_list) - 50
print(f"{min_set}")