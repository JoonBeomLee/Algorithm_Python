def solution(user_m, musicinfos):
    answer = []
    user_m_list = []
    for i, m in enumerate(user_m):
        if m == '#':
            user_m_list[-1] += '#'
        else:
            user_m_list.append(m)
    
    
    # music info 회문
    for music_info in musicinfos:
        music_info_list = music_info.split(",")
        
        music_st = list(map(int, (music_info_list[0].split(":"))))
        music_ed = list(map(int, (music_info_list[1].split(":"))))
        music_name = music_info_list[2]
        music_melody = music_info_list[3]
        
        # melody 재조정
        # '#' 조정
        melody_list = []
        for i, m in enumerate(music_melody):
            if m == '#':
                melody_list[-1] += '#'
            else:
                melody_list.append(m)

        # melody 재조정 - time 조정
        re_time_h = (music_ed[0] - music_st[0] + -1) if music_ed[1] - music_st[1] < 0 else (music_ed[0] - music_st[0])
        re_time_m = (60 + (music_ed[1] - music_st[1]) ) if music_ed[1] - music_st[1] < 0 else music_ed[1] - music_st[1]
        re_total_time = (60 * re_time_h) + re_time_m
        
        # melody 재조정 - melody 조정
        melody_idx = 0
        re_melody = []
        for idx in range(re_total_time):
            re_melody.append(melody_list[idx % len(melody_list)])
            

        # melody 판단         
        for m_idx, mld in enumerate(re_melody):   
            if re_melody[m_idx:m_idx+len(user_m_list)] == user_m_list:
                answer.append([music_name, re_total_time])
                break           
                
    re_answer = sorted(answer, key=lambda x : x[1], reverse=True)
    
    if len(re_answer) == 0: answer = "(None)"
    else:
        answer = re_answer[0][0]

    return answer