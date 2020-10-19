def solution(s):
    answer = ''
    
    spell_odd_idx = 0
    for spell in s:
    
        if spell == " ": 
            spell_odd_idx = 0
            answer += " "
            continue
            
        if spell_odd_idx % 2 == 0: answer += spell.upper()
        else: answer += spell.lower()
            
        spell_odd_idx += 1
        
    #print(answer)
    
    return answer