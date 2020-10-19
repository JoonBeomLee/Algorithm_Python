def solution(n):
    answer = 0

    for n_idx in str(n):
        answer += int(n_idx)

    return answer