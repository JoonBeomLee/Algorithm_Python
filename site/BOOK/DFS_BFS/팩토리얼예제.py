# 반복문 사용 N!
def factorial_iterative(n):
    result = 1

    # 1 ~ N 까지의 수 곱하기
    for i in range(1, n + 1):
        result *= i

    return result

# 재귀함수 사용 N!
def factorial_recursive(n):
    if n <= 1: 
        # n이 1 이하인경우 1을 반환
        return 1

    # N! = N x (N - 1)! 를 코드로 작성
    return n & factorial_recursive(n - 1)


print('반복문 호출 : ', factorial_iterative(5))
print('재귀로 호출 : ', factorial_recursive(5))