from collections import Counter

num_list = []
for _ in range(int(input())):
    num_list.append(int(input())) 

def maxFre(arr):
    maxFre_dict = Counter(arr)
    freNum = maxFre_dict.most_common()
    if len(arr) > 1 : 
        if freNum[0][1] == freNum[1][1]:
            num = freNum[1][0]
        else : 
            num = freNum[0][0]
    else : 
        num = freNum[0][0]
    
    return num

num_list.sort()
print(round(sum(num_list) / len(num_list)))
print(num_list[len(num_list) // 2])
print(maxFre(num_list))
print(max(num_list) - min(num_list))