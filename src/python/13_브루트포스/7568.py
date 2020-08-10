person_info = []
for _ in range(int(input())):
    w, h = input().split(" ")
    # 0 : 몸무게 
    # 1 : 키 
    # 2 : 랭킹
    person_info.append([w, h, 1])
    
for p1 in person_info:
    for p2 in person_info:
        if(p1 == p2): continue
        # p1의 키와 몸무게가 클경우 랭킹 상승
        if(p1[0] > p2[0] and p1[1] > p2[1]): p2[2] += 1
            
for p in person_info:
    print(p[2], end=" ")