NOTATION = '0123456789ABCDEF'

def dec_to_tri(dec_num):
    q, r = divmod(dec_num, 3)
    n = NOTATION[r]
    
    return dec_to_tri(q) + n if q else n

def tri_to_dec(tri_num):
    tri_len = len(tri_num) - 1
    dec_num = 0
    
    for tri in tri_num:
        dec_num += int(tri) * (3 ** tri_len)
        tri_len -= 1
        
    return dec_num
    
def solution(n):
    answer = 0
    
    tri = dec_to_tri(n)
    tri_rev = list(str(tri))
    tri_rev.reverse()
    tri_rev = ''.join(tri_rev)
    
    answer = tri_to_dec(tri_rev)
    
    return answer