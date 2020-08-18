# 참조 https://www.daleseo.com/sort-quick/
def quick_sort(arr):
    def sort(start, end):
        if end <= start: return

        mid = partition(start, end)
        sort(start, mid-1)
        sort(mid, end)

    def partition(start, end):
        pivot = arr[(start + end) // 2]

        # 시작과 끝이 서로 교차할때 까지 반복
        while start <= end:
            while arr[start] < pivot: start += 1 # 왼쪽의 데이터가 pivot보다 큰값을 찾으러감
            while arr[end] > pivot: end -= 1 # 오른쪽의 데이터가 pivot보다 작은값을 찾으러감

            # 위 두 while을 통과 후에도 끝나지 않을 경우
            # 잘못된(정렬되지 않은) 데이터가 있음
            # 두 값을 swap
            if start <= end:
                arr[start], arr[end] = arr[end], arr[start]
                # 교체후 다음 값을 확인하러 이동
                start += 1
                end -= 1

        return start

    return sort(0, len(arr)-1)

arr_list = []
for _ in range(int(input())):
    arr_list.append(int(input()))
    
quick_sort(arr_list)
for _ in arr_list:
    print(_)