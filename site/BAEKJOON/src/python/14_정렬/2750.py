# python sort 함수 사용
arr_list = []

for _ in range(int(input())):
    arr_list.append(int(input()))
    
arr_list.sort()

for _ in arr_list:
    print(_)

# quick sort 
def quick_sort(arr):
    if len(arr) <= 1: return arr
    
    pivot = arr[len(arr) // 2]
    smaller_arr, equal_arr, bigger_arr = [], [], []
    
    for num in arr:
        if num < pivot: smaller_arr.append(num)
        elif num > pivot: bigger_arr.append(num)
        else: equal_arr.append(num)
            
    return quick_sort(smaller_arr) + equal_arr + quick_sort(bigger_arr)

arr_list = []

for _ in range(int(input())):
    arr_list.append(int(input()))

quick_sorted_arr = quick_sort(arr_list)
for _ in quick_sorted_arr:
    print(_)