def hansu(nums):
    count = 0
    cha = 0
    
    for i in range(1, nums+1):
        if(i < 100): count += 1; continue
        tmps = list(str(i))
        
        cha = int(tmps[1]) - int(tmps[0])
        #print(tmps, cha)
        
        judge = False
        for j in range(len(tmps)-1):  
            #print(tmps[j], tmps[j+1], cha)   
        
            if( (int(tmps[j+1]) - int(tmps[j])) == int(cha)): judge= True
            else: judge = False; break
                
            #print(judge)
            
        if(judge): count = count + 1
        #print(judge, end="\n\n")
            
    return count

print(hansu(int(input())))