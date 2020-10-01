def solution(s):
    answer = ''

    str_len = len(s)
    
    # 짝수
    if str_len % 2 == 0:
        tmp = int(str_len / 2)
        answer = s[tmp-1] + s[tmp]
    # 홀수
    else:
        tmp = str_len // 2
        answer = s[tmp]
    
    return answer