def judge(string):
    lst_string = list(string)
    stack = []
    
    
    while len(lst_string) != 0:
        val = lst_string.pop(0)
    
        # 여는괄호
        if val in ["[", "(", "{"]:
            stack.append(val)
        # 닫는 괄호
        else:
            if not stack: 
                return False
            out = stack.pop()
            
            if out == "[" and val == "]": continue
            elif out == "(" and val == ")": continue
            elif out == "{" and val == "}": continue
            else:
                return False
    
    if stack: return False
    
    return True

def solution(s):
    answer = 0
    count = 0
    
    lst_string = list(s)
    
    while count < len(lst_string):
        if judge(lst_string): 
            answer += 1
            
        count += 1
        tmp = lst_string.pop(0)
        lst_string.append(tmp)
    
    return answer