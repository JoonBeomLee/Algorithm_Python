# N을 입력받기
N = int(input())

# N개의 정수를 입력받아 리스트에 저장
array = []
for i in range(N):
    array.append(int(input()))

# 파이썬 기본정렬 라이브러리 이용하여 정렬
array = sorted(array, reverse=True)

print(array)