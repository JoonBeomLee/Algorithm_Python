def solution(number, k):
    # 맨 앞 숫자 (number[0])
    num_stack = [number[0]]
    
    #print("pre :: ", num_stack[-1])
    
    # 입력된 맨앞을 제외한
    # 나머지 숫자 loop
    for num in number[1:]:
        #print("loop :: ",num)
        
        # 나머지 값이 stack 값보다 크면
        # 맨 앞의 값을 순차적으로 비교
        # 기존 값을 새로운 값으로 교체
        # 리스트 참조오류 나지 않도록
        while len(num_stack) > 0 and num_stack[-1] < num and k > 0:
            # 값을 한개 빼서 k는 1이 제거 
            k -= 1
                
            # 맨 앞 값이 작은 경우
            # 제거
            num_stack.pop()
            
        # 새로운 값 삽입
        num_stack.append(num)

    # 스택에 값이 남아 있을 경우
    # 나머지값 추가
    if k != 0:
        num_stack = num_stack[:-k]
        
    return ''.join(num_stack)