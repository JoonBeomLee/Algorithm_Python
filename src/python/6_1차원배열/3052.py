nums = list()
tmp = -1

for i in range(0, 10, 1):
    tmp = int(input()) % 42
    nums.append(tmp)

nums = list(set(nums))
            
print(len(nums))