import itertools
import copy

def solution(expression):
    answer = 0
    answer_list = []
    exp_list = []
    op_list = []
    tmp_num = ''
    
    for exp in expression:
        if exp.isnumeric(): tmp_num += exp
        else:
            exp_list.append(tmp_num)
            exp_list.append(exp)
            op_list.append(exp)
            
            tmp_num = ''
            
    exp_list.append(tmp_num)
    seted_op_list = list(set(op_list))
    seted_op_list = list(map(list, itertools.permutations(seted_op_list, len(seted_op_list))))
    
    #print(exp_list)
    #print(list(set(op_list)))
    #print(seted_op_list)
    
    # 연산자 조합 리스트 회문
    for set_op_list in seted_op_list:
        tmp_exp_list = copy.copy(exp_list)
        calc_result = 0
        
        
        #print(set_op_list)
        
        # 선택된 연산자 리스트 
        # 세부 회문
        for op in set_op_list:
            
            exp_idx = 0
            # 수식 회문
            while True:
                # 모든 값이 마무리 될 경우
                if len(tmp_exp_list) == 1: break
                
                # 연산할 연산자가 없을경우 => 정지
                if op not in tmp_exp_list: break
                    
                # 마지막까지 회문 할경우 0으로 초기화
                if exp_idx == len(tmp_exp_list): exp_idx = 0

                # 연산자가 대상 연산자일 경우
                if op == tmp_exp_list[exp_idx]:
                    # 실제 연산
                    if op == '+':
                        tmp_exp_list[exp_idx - 1] = int(tmp_exp_list[exp_idx - 1]) + int(tmp_exp_list[exp_idx+1])
                        
                    if op == '-':
                        tmp_exp_list[exp_idx - 1] = int(tmp_exp_list[exp_idx - 1]) - int(tmp_exp_list[exp_idx+1]) 
                        
                    if op == '*':
                        tmp_exp_list[exp_idx - 1] = int(tmp_exp_list[exp_idx - 1]) * int(tmp_exp_list[exp_idx+1])
                        
                        
                    # 연산후 수식 제거
                    del tmp_exp_list[exp_idx]
                    del tmp_exp_list[exp_idx]
                    
                else:
                    exp_idx += 1
        
            answer_list.append(abs(int(tmp_exp_list[0])))
        
    return max(answer_list)