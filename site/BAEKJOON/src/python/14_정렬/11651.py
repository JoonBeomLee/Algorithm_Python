COUNT = int(input())
pos_list = []

for _ in range(COUNT):
    pos_list.append(list(map(int, input().split())))
                    
pos_list.sort(key=lambda x : (x[1], x[0]))      
for nums in pos_list:
    print(f'{nums[0]} {nums[1]}')            