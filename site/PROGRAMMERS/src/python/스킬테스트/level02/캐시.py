import copy

def solution(cacheSize, cities):
    answer = 0
    cache = [["", 0] for _ in range(cacheSize)]
    job_idx = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    # 작업 시작
    for city in cities:
        # job count를 제외한
        # data만 반환
        tmp = [data[0] for data in cache]
        
        # 작업 대상 도시가 cahce에 없을 경우
        if city.lower() not in tmp:
            # cache가 비어 있는 경우
            if "" in tmp:
                # 빈공간에 city 채움
                cache_idx = tmp.index("")
                cache[cache_idx] = copy.copy([city.lower(), job_idx])
                
                job_idx += 1
                
                # cache miss => runTime += 5
                answer += 5
            # 공간 없을때
            else:
                # LRU [가장 사용이 되지 않은]
                cache = sorted(cache, key=lambda data: copy.copy(data[1]), reverse=True)
                cache[-1] = [city.lower(), job_idx]
                
                job_idx += 1
                
                # cache miss => runTime += 5
                answer += 5
                
        # 작업 대상 도시가 cache에 있을 경우
        else:
            tmp = [data[0] for data in cache]
            tmp_idx = tmp.index(city.lower())
            
            # 작업 수행 
            cache[tmp_idx][1] = job_idx
            job_idx += 1
            
            # cache hit => runTime += 1
            answer += 1
                
        
    return answer