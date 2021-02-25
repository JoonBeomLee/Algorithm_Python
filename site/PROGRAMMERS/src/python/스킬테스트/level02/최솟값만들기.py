def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    for idx in range(len(A)):
        answer += A[idx] * B[idx]

    return answer