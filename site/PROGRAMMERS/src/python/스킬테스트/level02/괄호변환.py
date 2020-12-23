from collections import deque

# 괄호 유효성 체크
def is_correct(_str): 
    stack_list = []
    for s in _str:
        if s == '(':
            stack_list.append(s)
        elif stack_list:
            stack_list.pop()
    return not stack_list

# 문자열 u, v 분할
def str_split(_str): 
    que = deque(_str)
    left, right = 0, 0
    u_str, v_str = "", ""
    
    # que 회문
    while que:  
        u_str += que.popleft()
        if u_str[-1] == '(':
            left += 1
        else:
            right += 1
        
        # 균형 잡힌 괄호
        if left == right:
            break  

    v_str = ''.join(list(que))
    return u_str, v_str

# 뒤집기
def reverse(u):  
    return ''.join([')' if s == '(' else '('for s in u])

def recursive(string):
    # 1번
    if string == '': 
        return ''
    # 2번
    u, v = str_split(string) 
    
    # 3번
    if is_correct(u):  
        return u + recursive(v)
    
    # 4번
    else:  
        return '(' + recursive(v) + ')' + reverse(u[1:-1])

def solution(p):
    return p if is_correct(p) else recursive(p)