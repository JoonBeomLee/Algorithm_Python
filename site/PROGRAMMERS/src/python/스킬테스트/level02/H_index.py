def solution(citations):
    citations.sort(reverse=True)
    # ( index[1 ~ N] | 인용수 )중 작은 값으로 list 생성
    sorted_papers = list(map(min, enumerate(citations, start=1)))   
    
    # 그 중 큰값 = answer
    # 큰 값 => ( index | 인용수 )
    # 역전된 지점 = 닶
    answer = max(sorted_papers)
    return answer