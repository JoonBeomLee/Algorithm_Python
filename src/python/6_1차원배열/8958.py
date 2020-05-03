count = int(input())

for i in range(count):
    nums = list()
    nums = list(input())
    
    tmp_score = 0; total_score = 0
    for j in nums:
        if(j == "O"): tmp_score = tmp_score + 1
        else: tmp_score = 0
            
        total_score = total_score + tmp_score
            
    print(total_score)