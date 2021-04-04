from datetime import datetime, timedelta

def solution(m, musicinfos):
    answer = ''
    YEAR = 2021
    MONTH = 4
    DAY = 4
    
    # music info 회문
    for music_info in musicinfos:
        music_info_list = music_info.split(",")
        
        music_st = list(map(int, (music_info_list[0].split(":"))))
        music_ed = list(map(int, (music_info_list[1].split(":"))))
        music_name = music_info_list[2]
        music_melody = music_info_list[3]
        
        # melody 재조정                
        
        if len(m) > len(music_melody):
            if music_melody in m: 
                answer = music_name
                break
        else:
            if m in music_melody: 
                answer = music_name
                break
                
    return answer