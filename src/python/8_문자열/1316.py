count = int(input())
check_count = 0

for i in range(count):
    tmps = input(); tmps = list(tmps)
    judge = True
    
    for j in range(0, len(tmps)):
        dist = 0
        for k in range(j, len(tmps)):           
            if( (tmps[j] == tmps[k]) and (dist != 0)): judge = False; break
            if(tmps[j] == tmps[k]): dist = 0           
            else: dist += 1
            
    if (judge): check_count += 1
        
print(check_count)