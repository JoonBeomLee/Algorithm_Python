count = int(input())

for i in range(count):
    nums = list()
    nums = list(map(int, input().split(" ")))
    count_f = nums[0]; nums.pop(0)
    
    avg = sum(nums) / count_f
    result = sum(i > avg for i in nums)
    result = round( (result / count_f), 5)
    result = round( (result * 100) , 3)

    print("%0.3f" %(result), end="");print("%")