count = int(input())
nums = list()

nums = list(map(int, input().split()))
    
max_point = max(nums)

for i in range(len(nums)):
    nums[i] = nums[i] / max_point * 100

print(round(sum(nums) / len(nums), 3))