test_case_count = int(input())
test_case = []

# inpu data
# test_case H:[0] W:[1] N:[2]
for i in range(test_case_count):
    H, W, N = map(int, input().split(" "))
    
    floorNum = str( H if(N % H == 0) else N % H )
    roomNum = str( (N // H) if ((N % H) == 0) else ((N // H) + 1) )
    
    roomNum = "0" + roomNum  if len(roomNum) == 1 else roomNum 
    
    print(floorNum+roomNum)