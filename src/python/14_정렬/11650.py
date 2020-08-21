def sel_sort(arr):
    for i in range(len(arr)):
        for j in range(len((arr))):
            if i == j: continue
            if arr[i][0] < arr[j][0]: arr[i], arr[j] = arr[j], arr[i]
            if arr[i][0] == arr[j][0]:
                if arr[i][1] < arr[j][1]: arr[i], arr[j] = arr[j], arr[i]
                    
    return arr

COUNT = int(input())
pos_list = []

for _ in range(COUNT):
    pos_list.append(list(map(int, input().split())))
                    
sorted_pos_list = sel_sort(pos_list)
for nums in sorted_pos_list:
    print(f'{nums[0]} {nums[1]}')