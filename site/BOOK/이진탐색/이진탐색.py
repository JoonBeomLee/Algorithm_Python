# 재귀로 구현
def binary_search(array, target, st, ed):
    if st > ed: return None

    mid = (st + ed) // 2

    if array[mid] == target: return mid
    elif array[mid] > target:
        return binary_search(array, target, st, mid -1)
    else:
        return binary_search(array, target, mid + 1, ed)

N, target = list(map, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, N - 1)
if result == None: print("target is None")
else: print(result + 1)


# 반복문으로 구현
def binary_search_loop(array, target, st, ed):
    while st <= ed:
        mid = (st + ed) // 2

        if array[mid] == target: return mid
        elif array[mid] > target: ed = mid - 1
        else: st = mid + 1

    return None

result = binary_search_loop(array, target, 0, N - 1)
if result == None: print("target is None")
else: print(result + 1)
