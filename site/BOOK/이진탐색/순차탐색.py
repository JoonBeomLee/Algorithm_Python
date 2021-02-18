# 순차 탐색
def sequential_search(n, target, array):
    # 원소 순차 탐색
    for i in range(n):
        # search 대상일경우
        if array[i] == target:
            # 현재 위치 반환 (배열 인덱스는 0부터 시작하므로 +1)
            return i + 1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열 입력하세요.")
input_data = input().split()
n = int(input_data[0])  # 원소개수
target = input_data[1]  # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분읜 띄어쓰기 한칸으로 합니다.")
array = input().split()

# 순차 탐색 결과 출력
print(sequential_search(n, target, array))