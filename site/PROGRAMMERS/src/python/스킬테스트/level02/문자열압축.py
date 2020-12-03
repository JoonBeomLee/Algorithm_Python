def solution(s):
    answer = 0
    origin_len = len(s)
    zip_list = []
    
    # 1자리 문자열 예외처리
    if origin_len == 1: return 1