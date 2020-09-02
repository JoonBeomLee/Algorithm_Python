N = int(input())
result = 0

for nums in range(N):
    sum_N = nums
    for num in str(nums):
        sum_N += int(num)
        
    if(sum_N == N): result = nums; break
        
print(result)