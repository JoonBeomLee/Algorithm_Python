def solution(nums):
    # 최대로 가져 갈수 있는 포켓몬 수
    max_limit = len(nums) // 2
    # 포켓몬 종류 set() 을 통한 중복제거
    seted_nums = list(set(nums))
    # 데려갈 수 있는 포켓몬 수
    avail_count = len(seted_nums)
    
    # 데려갈 수 있는 포켓몬 수는 limit를 넘을 수 없다
    answer = avail_count if max_limit > avail_count else max_limit
    
    return answer
