def solution(records):
    answer = []
    log = []
    id_dict = {}
    
    for record in records:
        # rc_list[0] = [Enter | Leave | Change]
        # rc_list[1] = [uid]
        # rc_list[2] = [name] [Leave 명령일때는 name 출력 x]
        rc_list = record.split()
        cmd = rc_list[0]
        uid = rc_list[1]
        
        # cmd 판별
        # 방입장
        if cmd == "Enter":
            # 로그 기록
            log.append([uid, "님이 들어왔습니다."])
            
            # 닉네임 갱신
            id_dict[uid] = rc_list[2]
        
        # 닉네임 변경
        elif cmd == "Change":
            # 닉네임 갱신
            id_dict[uid] = rc_list[2]
            
        # 방 퇴장
        elif cmd == "Leave":
            log.append([uid, "님이 나갔습니다."])
                
    # log 처리
    for lg in log:
        answer.append(f"{id_dict[lg[0]]}{lg[1]}")
    
    return answer