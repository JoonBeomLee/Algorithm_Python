# 이진탐색
# 최소(0시간) ~ 최대(max(times) * N)[가장 긴 심사대에서 모두 심사할 경우 소요되는 시간]
# 임의의 총 심사 시간을 [최소 ~ 최대] 의 중간값으로 지정한다
# 각 심사대가 mid 시간만큼 동안에 처리할 수 있는 최대 심사 인원수를 구해 누적한다.
# 이것은 mid 시간동안 총 심사할 수 있는 인원이 된다.
# 처리할 수 있는 인원 수가 목표 인원 수 N보다 작으면 left => mid + 1 (처리할 인원 수를 늘리기 위함)
# 처리할 수 있는 인원 수가 목표 인원 수 N보다 크면 right => mid - 1 (심사 시간을 줄이기 위함)
# 이때, mid가, 저장해둔 심사 시간 answer보다 짧은 시간이면 answer 갱신
def solution(peoples, times):
    left = 0
    right = max(times) * peoples
    
    answer = right
    
    while left <= right:
        task_N = 0
        mid = (left + right) // 2 # 임의의 총 심사시간
        
        # 지정된 mid 시간대에서 처리할 수 있는 인원 수
        for time in times:
            task_N += mid // time
            
        # 처리할 인원수가 남은 경우 범위 재조정
        if task_N < peoples:
            left = mid + 1
        # 모두 처리 했을 경우 최소값 서치
        else:
            right = mid - 1
            
            # answer는 가능한 값들중 최소값을 유지한다
            if mid <= answer:
                answer = mid
                
    return answer
            
        