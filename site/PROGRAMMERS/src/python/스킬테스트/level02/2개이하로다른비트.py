def convert2bit(num):    
    return bin(num)[2:]

def solution(numbers):
    answer = []
    
    for num in numbers:
        bin_num = list('0' + str(convert2bit(num)))
        
        # 짝수
        if num % 2 == 0:
            answer.append(num + 1)
            
        # 홀수
        else:
            #print("debug", num, bin_num)

            first_zero = False
            
            for b_num in range(len(bin_num) - 1, -1, -1):
                #print(bin_num, b_num, bin_num[b_num])
                
                if first_zero == False and bin_num[b_num] == '0':
                    #print(b_num)
                    
                    bin_num[b_num] = '1'
                    bin_num[b_num + 1] = '0'
                    
                    first_zero = True
                    
                    
            bin_str = ''.join(bin_num)
            bin_num = int(bin_str, 2)
            #print("홀수", bin_num, int(bin_str, 2))
            answer.append(bin_num)
        
    #print(answer)
    
    return answer