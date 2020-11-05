NOTATION = "0123456789"

def str1_xor_str2(str1, str2):
    result = ""
    
    for idx in range(len(str1)):
        tmp = int(str1[idx]) or int(str2[idx])
        result += "#" if tmp == 1 else " "
    
    return result
        
def dec_to_bin(dec):
    q, r = divmod(dec, 2)
    n = NOTATION[r]
    
    return dec_to_bin(q) + n if q else n

def solution(n, arr1, arr2):
    answer = []
    tmp_arr = []
    
    for a_idx in arr1:
        tmp = dec_to_bin(a_idx)
        zero_padding = "0" * (n - len(tmp))
        tmp = str(zero_padding) + tmp
        
        tmp_arr.append(tmp)
    
    idx = 0
    for b_idx in arr2:
        tmp = dec_to_bin(b_idx)
        zero_padding = "0" * (n - len(tmp))
        tmp = str(zero_padding) + tmp
        
        answer.append(str1_xor_str2(tmp, tmp_arr[idx]))  
        idx += 1
        
    return answer