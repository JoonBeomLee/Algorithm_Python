def solution(s):
    answer = 0
    origin_len = len(s)
    zip_list = []
    
    # 1자리 문자열 예외처리
    if origin_len == 1: return 1
    
    # slice 단위 1 ~ len//2
    for per in range(1, origin_len // 2 + 1):
        zip_str = []   # per 단위로 자른 문자열 담는 tmp 리스트  
        count = 1      # 같은 문자열 반복시 count
        
        # st, ed, step
        for idx in range(0, origin_len, per):
            tg_str = s[idx:idx+per]     # 대상 문자열
            
            # 대상 문자열과 다음 문자열이 같을 경우 count ++             
            if tg_str == s[idx+per : idx+2*per]:
                count += 1
            
            # 다를경우 2가지 경우 판별
            elif tg_str != s[idx+per : idx+2*per]:
                
                # 1이 아닐경우 (2이상으로 압축됬을 경우)
                # 압축된만큼 count STR 로 출력
                if count != 1:
                    zip_str.append(f'{count}{tg_str}')
            
    return answer