def solution(string):
    answer = 0
    check_stack = []

    # 첫문자 stack에 삽입
    check_stack.append(string[0])
    string = string[1:]
    
    for s in string:
        if len(check_stack) == 0: check_stack.append(s)
        # 같은 문자일 경우 stack 맨앞 문자 제거
        elif s == check_stack[-1]:
            check_stack.pop()
        # 다른 문자일 경우 추가
        else:
            check_stack.append(s)
        
    # 모두 제거된 경우 stop
    if len(check_stack) == 0: 
        answer = 1       

    return answer