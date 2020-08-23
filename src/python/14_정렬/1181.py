COUNT = int(input())
str_list = []

for _ in range(COUNT):
    str_list.append(input())
       
str_list = list(set(str_list)) # 중복제거
str_list.sort(key=lambda x : (len(x), x))      
for strs in str_list:
    print(strs)            