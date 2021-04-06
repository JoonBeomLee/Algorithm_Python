def solution(message):
    answer = []
    m_dict = {}
    
    # init dict
    for msg in message:
        m_dict[msg] = ord(msg) - 64
    
    word_count = 0
    word_idx = 0
    new_word_idx = 27
    target_word = ""
    next_word = ""
    more_word = False
    
    while True:
        if word_idx >= len(message): break
            
        if more_word:
            target_word = target_word + next_word
            word_idx += 1
        else:
            target_word = message[word_idx]
        
        if word_idx + 1 >= len(message): break
            
        next_word = message[word_idx + 1]
        
        if target_word in m_dict and target_word + next_word not in m_dict:           
            answer.append(m_dict[target_word])
            m_dict[target_word + next_word] = new_word_idx
            
            new_word_idx += 1
            word_idx += 1
            more_word = False
            continue
            
        if target_word + next_word in m_dict:
            more_word = True

    answer.append(m_dict[target_word])   
            
    return answer