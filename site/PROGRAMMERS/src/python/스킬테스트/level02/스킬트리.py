def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        
        # skill tree 검증 판단
        tree_judge = True
        tmp_user_skill = list(skill)

        # 처음 skill 선택
        user_skill = tmp_user_skill.pop(0)

        for tg_skill in skill_tree:
            # 정상적인 트리
            # 다음 스킬을 결정
            if tg_skill == user_skill:
                # 정상적인 트리 done
                if len(tmp_user_skill) == 0: break
                # 현재단계 정상 => 다음 스킬 검색
                else:
                    user_skill = tmp_user_skill.pop(0)
                    
            # 잘못된 트리
            # 선행스킬 이전에 다른스킬이 있는 경우
            elif tg_skill in tmp_user_skill:
                tree_judge = False
                break


        if tree_judge: answer += 1
                    
    
    return answer