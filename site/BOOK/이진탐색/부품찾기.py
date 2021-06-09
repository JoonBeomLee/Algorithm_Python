# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, st, ed):
    while st <= ed:
        mid = (st + ed) // 2

        # target search
        if array[mid] == target: return mid
        # smaller target
        elif array[mid] > target:
            ed = mid -1
        # bigger target
        else:
            st = mid + 1

# 가게의 부품 개수 입력
N = int(input())
# 가게 부품 list에 저장
store_list = list(map(int, input().split()))
# 이진탐색 위한 정렬
store_list.sort()

# 손님 요청 부품 개수
M = int(input())
# 손님 요청 부품 리스트
customer_list = list(map(int, input().split()))

# 손님 요청 부품 하나씩 확인
for item in customer_list:

    result = binary_search(customer_list, item, 0, N-1)

    if result != None: print("yes", end=" ")
    else: print("no", end=" ")


# 계수 정렬 방법
# 모든 원소의 번호를 포함할 수 있는 크기의 리스트 생성 후
# 리스트 인덱스에 직접 접근하여 부품 여부 확인