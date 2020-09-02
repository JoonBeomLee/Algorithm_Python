num_list = []
list_max = 5

for i in range(list_max):
    inpt_num = int(input())
    
    if(inpt_num < 40): inpt_num = 40
    num_list.append(inpt_num)

avg = sum(num_list) / len(num_list)
print(f"{avg:.0f}")