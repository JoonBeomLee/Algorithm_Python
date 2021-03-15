def solution(n, words):
    answer = []

    player = 1
    turn = 1
    
    # 중복 문자 체크
    seted_words = list(set(words))
    
    # 중복 문자 체크 실행
    if len(seted_words) != len(words):
        re_word = []
        for w_idx, word in enumerate(words):
            if word not in re_word:
                re_word.append(word)
            # 중복 문자 위치
            else:
                answer = [player, turn]
                return answer
                
            # 1회 turn 
            if w_idx % n == n - 1:
                player = 1
                turn += 1
            # 다음 player
            else:
                player += 1
                
    # 끝말잇기 실패
    player = 2
    turn = 1
    for w_idx, word in enumerate(words):
        # 첫턴은 패스
        if w_idx == 0: continue
        
        # 현재 단어 첫 spell이
        # 이전 단어 마지막 spell과 다를 경우 
        # 끝말 잇기 실패
        if word[0] != words[w_idx-1][-1]:
            
            answer = [player, turn]
            return answer
        
        # 1회 turn 
        if w_idx % n == n - 1:
            player = 1
            turn += 1
        # 다음 player
        else:
            player += 1
        

    return [0, 0]