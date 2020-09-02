def self_num(num):
    num = str(num)
    tmp = list()
    tmp_sum = 0
    
    if(int(num) > 10000): return 0
    elif(int(num) > 1000): 
        tmp = list(map(int, num))
        tmp_sum = int(num) + int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
        
    elif(int(num) > 100): 
        tmp = list(map(int, num))
        tmp_sum = int(num) + int(num[0]) + int(num[1]) + int(num[2])

    elif(int(num) > 10): 
        tmp = list(map(int, num))
        tmp_sum = int(num) + int(num[0]) + int(num[1])

    else: 
        tmp = list(map(int, num))
        tmp_sum = int(num) + int(num[0])

            
    return tmp_sum

check = [0] * 10035
for i in range(10000):
    check[self_num(i)-1] = 1
    
for i in range(10000):
    if(check[i] == 0): print(i +1)