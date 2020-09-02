count, miNum = input().split(" ")
count = int(count); miNum = int(miNum)

num_list = input().split(" ")

for i in range(count):
    if int(num_list[i]) < miNum : print(num_list[i])