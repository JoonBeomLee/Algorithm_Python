n1, n2 = input().split(" ")
n1 = list(n1); n2 = list(n2)

n1.reverse(); n2.reverse()
n1 = "".join(n1); n2 = "".join(n2)

if(int(n1) > int(n2)): print(n1)
else: print(n2)