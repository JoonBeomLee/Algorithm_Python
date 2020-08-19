# counting sort
import sys
LIST_LEN = 10001
num_list = [0] * LIST_LEN

for _ in range(int(input())):
    num_list[int(input())] += 1
    
for num in range(LIST_LEN):
    for count in range(num_list[num]):
        sys.stdout.write(f'{num}\n')