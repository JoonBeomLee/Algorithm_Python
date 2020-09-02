sumNum = int(input())
n1 = int(sumNum/10); n2 = int(sumNum%10)
count = 0
tmp = 0

while True:
    tmp = n1 + n2
    n1 = n2; n2 = tmp % 10
    tmp = n1*10 + n2
    #print(count, n1, n2, tmp, sumNum)
    count = count + 1
    
    if (sumNum == tmp): break
    
    