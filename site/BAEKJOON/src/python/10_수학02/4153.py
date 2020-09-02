while True:
    Tri = list(map(int, input().split(" ")))
    Tri.sort()
    
    if Tri[0] == 0 and Tri[1] == 0 and Tri[2] == 0: break
    elif Tri[0]**2 + Tri[1]**2 == Tri[2]**2: print("right")
    else: print("wrong")