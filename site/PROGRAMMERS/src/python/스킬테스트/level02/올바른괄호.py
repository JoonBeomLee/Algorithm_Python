def solution(sign_list):
    answer = True
    
    print(sign_list)
    
    stack = []
    for sign in sign_list:
        if sign == ')': 
            if len(stack) <= 0: 
                answer = False
                break
            stack.pop(-1)
        else: stack.append('(')

    if len(stack) == 0 and answer != False: answer = True
    else: answer = False    
    
    return answer