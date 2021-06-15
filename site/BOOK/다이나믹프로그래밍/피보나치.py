# 피보나치 함수 - 재귀함수
# 점화식을 기준으로 작성
# N 이 커질수록 연산 경과 시간은 기하급수적으로 증가
def fibo(N):
    if N == 1 or N == 2: return 1

    return fibo(N - 1) + fibo(N - 2)

# 피보나치 - 메모제이션(한번 수행한 결과값을 저장하여 중복 연산 방지)
# 한 번 계산된 결과를 메모제이션 위한 리스트
RAM = [0] * 100

def fibo(N):
    # 종료 조건 (1 | 2일때 1반환)
    if N == 1 or N == 2: return 1

    # 이미 계산된 문제라면 그대로 반환
    if RAM[N] != 0:
        return RAM[N]
    
    # 아직 계산하지 않은 문제라면 연산후 저장
    RAM[N] = fibo(N - 1) + fibo(N - 2)
    
    return RAM{N}