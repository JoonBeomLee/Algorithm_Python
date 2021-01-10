def solution(people, limit):
    # 운영된 보트 카운트
    answer = 0
    
    # 갇힌 인원 idx
    l_idx = 0
    r_idx = len(people) - 1
    
    # 탈출인원 카운트
    out_count = 0
    # 갇힌 인원
    people_count = len(people)
    
    # 몸무게 큰 순으로 정렬
    people.sort(reverse=True)
    
    while True:
        # 남은 인원이 없을 경우
        if out_count >= people_count: break
            
        # 가장 큰 무게 + 가장 작은 무게 <= limit
        if people[l_idx] + people[r_idx] <= limit:             
            # 앞, 뒤 index 조정
            l_idx += 1
            r_idx -= 1           
            
            # 탈출 인원
            out_count += 2
            # 보트
            answer += 1
        # 아닌 경우
        # 무게가 많이 나가는 인원 탈출
        else:
            # 앞 index 조정
            l_idx += 1
            # 탈출 인원 카운트
            out_count += 1
            # 보트 카운트
            answer += 1
    
    return answer