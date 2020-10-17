import datetime

YEAR = 2016

def solution(a, b):
    week_arr = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    date_info = datetime.datetime(YEAR, a, b)
    week_idx = date_info.weekday()
    
    answer = week_arr[week_idx]
    
    return answer