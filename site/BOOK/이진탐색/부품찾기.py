# solve - 1 
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


# solve - 2 
# 계수 정렬 방법
# 모든 원소의 번호를 포함할 수 있는 크기의 리스트 생성 후
# 리스트 인덱스에 직접 접근하여 부품 여부 확인
N = int(input())
array = [0] * 100001

# 가게에 있는 전체 부품 번호 저장
for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())

# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인요청한 부품번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1: print('yes', end=" ")
    else: print("no", end=" ")


# slove - 3
# 단순히 특정한 수가 한번이라도 등장 여부를 검사하면 되므로
# 집합 자료형을 이용해서 문제를 해결할 수 있다
# set() 함수는 집합 자료형을 초기화할 때 사용
N = int(input()) # N(가게의 부품 개수)을 입력받기
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

# M(손님이 확인 요청한 부품 개수)을 입력받기
M = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x: 
     # 해당 부품이 존재하는지 확인
    if i in array: print('yes', end=" ")
    else: print("no", end=" ")