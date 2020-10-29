def solution(x):
    answer = True
    x_str = str(x)
    position_sum = 0
    
    for x_spell in x_str:
        position_sum += int(x_spell)
        
    if x % position_sum != 0: answer = False
    
    return answer